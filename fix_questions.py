"""Post-review fixes for the full question set (run once, MODE=full).

  * regenerate q075 and q215, which repeated 4+ words of their paper title
  * replace q014, whose source paper was already a pilot source, with a new source paper
    drawn at random (seed 17) from corpus papers that are not a source, not a planted
    neighbour of any source and not a pilot paper

Same question model and the same instructions as make_questions.py; the only addition is a
line telling the model which title phrase not to reuse.
"""
from __future__ import annotations

import csv
import json
import random

import collect_papers as cp
import config
import llm
from make_questions import SYSTEM, TYPES, overlap

REWRITE = ["q075", "q215"]
REPLACE = "q014"


def ask(paper: dict, kind: str, avoid: str = "") -> str:
    user = f"Title: {paper['title']}\nAbstract: {paper['abstract']}\n\nStyle: {TYPES[kind]}"
    if avoid:
        user += f"\n\nDo not reuse this wording from the title, even partly: {avoid}"
    text, _ = llm.complete(config.QUESTION_MODEL, SYSTEM, user, max_tokens=600)
    q = str((llm.extract_json(text) or {}).get("question", "")).strip()
    plain = text.strip().strip('"')
    return q or (plain if "\n" not in plain and plain.endswith("?") else "")


def main() -> None:
    papers = [json.loads(l) for l in open(config.DATA / "papers.jsonl", encoding="utf-8")]
    by_id = {p["id"]: p for p in papers}
    questions = [json.loads(l) for l in open(config.DATA / "questions.jsonl", encoding="utf-8")]
    qmap = {q["qid"]: q for q in questions}
    kinds = list(TYPES)

    for qid in REWRITE:
        q = qmap[qid]
        p = by_id[q["gold_id"]]
        new = ask(p, q["type"], avoid=p["title"])
        print(f"{qid} OLD: {q['question']}\n{qid} NEW: {new}\n")
        q["question"], q["title_overlap"] = new, round(overlap(new, p["title"]), 2)

    # replacement source for q014
    old = qmap[REPLACE]
    pilot = {json.loads(l)["gold_id"] for l in open(config.ROOT / "data" / "questions.jsonl")}
    pilot |= {json.loads(l)["id"] for l in open(config.ROOT / "data" / "papers.jsonl")}
    sources = json.loads((config.DATA / "sources.json").read_text())
    vectors = cp.tfidf_vectors(papers)
    planted = set()
    for s in sources:
        planted.update(cp.nearest(by_id[s], papers, vectors, config.DISTRACTORS_PER_SOURCE, set(sources)))
    eligible = sorted(p["id"] for p in papers
                      if p["id"] not in set(sources) | planted | pilot)
    new_id = random.Random(17).choice(eligible)
    p = by_id[new_id]
    kind = kinds[int(REPLACE[1:]) % 3]
    text = ask(p, kind)
    print(f"{REPLACE} OLD source {old['gold_id']}: {old['question']}")
    print(f"{REPLACE} NEW source {new_id} [{kind}]: {p['title']}\n  Q: {text}\n  ({len(eligible)} eligible papers)\n")
    qmap[REPLACE] = {"qid": REPLACE, "gold_id": new_id, "type": kind, "question": text,
                     "title_overlap": round(overlap(text, p["title"]), 2), "gold_title": p["title"]}
    sources[sources.index(old["gold_id"])] = new_id
    (config.DATA / "sources.json").write_text(json.dumps(sources))

    with open(config.DATA / "questions.jsonl", "w", encoding="utf-8") as f:
        for q in questions:
            f.write(json.dumps(qmap[q["qid"]]) + "\n")
    rows = list(csv.reader(open(config.DATA / "questions_review.csv", encoding="utf-8")))
    head = rows[0]
    ix = {h: i for i, h in enumerate(head)}
    for r in rows[1:]:
        if r[0] in REWRITE + [REPLACE]:
            q = qmap[r[0]]
            r[ix["type"]], r[ix["question"]] = q["type"], q["question"]
            r[ix["gold_title"]], r[ix["title_overlap"]] = q["gold_title"], q["title_overlap"]
            r[ix["ok (1/0)"]] = ""
            r[ix["other_papers_that_also_answer"]] = ""
            r[ix["notes"]] = "REWRITTEN after review; needs a fresh ok value"
    csv.writer(open(config.DATA / "questions_review.csv", "w", newline="", encoding="utf-8")).writerows(rows)
    print(f"spend ${llm.LEDGER.usd:.4f}")


if __name__ == "__main__":
    main()
