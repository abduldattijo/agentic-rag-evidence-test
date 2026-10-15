"""Retry the source papers that got no question in make_questions.py (reply did not parse).

    MODE=full python retry_skipped.py

Same model, same instructions and same question type as the original rotation; only the output
limit is higher and a bare-question reply (no JSON) is accepted. That bare reply, not a
truncated one, is why these five were skipped the first time. Existing questions are kept; new rows are appended to both files.
"""
from __future__ import annotations

import csv
import json

import config
import llm
from make_questions import SYSTEM, TYPES, overlap


def main() -> None:
    papers = {json.loads(l)["id"]: json.loads(l) for l in open(config.DATA / "papers.jsonl", encoding="utf-8")}
    sources = json.loads((config.DATA / "sources.json").read_text())[:config.N_QUESTIONS]
    have = [json.loads(l) for l in open(config.DATA / "questions.jsonl", encoding="utf-8")]
    done = {r["gold_id"] for r in have}
    kinds = list(TYPES)
    new = []
    for i, pid in enumerate(sources):
        if pid in done:
            continue
        p, kind = papers[pid], kinds[i % len(kinds)]
        user = f"Title: {p['title']}\nAbstract: {p['abstract']}\n\nStyle: {TYPES[kind]}"
        text, _ = llm.complete(config.QUESTION_MODEL, SYSTEM, user, max_tokens=600)
        q = str((llm.extract_json(text) or {}).get("question", "")).strip()
        plain = text.strip().strip('"')
        if not q and "\n" not in plain and plain.endswith("?"):
            q = plain          # the model answered with the bare question instead of JSON
        if not q:
            print(f"  still no question for {pid}; raw reply: {text[:300]!r}")
            continue
        new.append({"qid": f"q{i:03d}", "gold_id": pid, "type": kind, "question": q,
                    "title_overlap": round(overlap(q, p["title"]), 2), "gold_title": p["title"]})
        print(f"{new[-1]['qid']} [{kind}] {q}")
    with open(config.DATA / "questions.jsonl", "a", encoding="utf-8") as f:
        for r in new:
            f.write(json.dumps(r) + "\n")
    with open(config.DATA / "questions_review.csv", "a", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        for r in new:
            w.writerow([r["qid"], r["type"], r["question"], r["gold_title"], r["title_overlap"], "", "", ""])
    print(f"added {len(new)} questions. spend ${llm.LEDGER.usd:.4f}")


if __name__ == "__main__":
    main()
