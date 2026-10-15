"""Step 2: write one question per sampled paper, with that paper as the known answer.

    python make_questions.py

Outputs
  data/questions.jsonl        what the evaluation reads
  data/questions_review.csv   open this and hand-check every row (see PLAN.md, step 3)

Question types rotate so the set is not all easy keyword matches:
  specific  names a method or setting but does not copy the title
  problem   describes the problem the paper solves, no method named
  vague     the half-remembered way a person would ask for it
"""
from __future__ import annotations

import csv
import json
import random
import re

import config
import llm

TYPES = {
    "specific": "Ask about the specific method or setting the paper studies, in your own words.",
    "problem": "Describe the problem the paper solves without naming its method.",
    "vague": "Ask the way a person half-remembering the paper would: short and imprecise.",
}

SYSTEM = ("You write search questions for a test of paper retrieval. Given one paper, write ONE "
          "question that this paper answers. Never copy the title or any phrase of 4+ words from "
          "it. Reply with only JSON: {\"question\": \"...\"}.")


def bigrams(text: str) -> set:
    w = re.findall(r"[a-z0-9]+", text.lower())
    return set(zip(w, w[1:]))


def overlap(question: str, title: str) -> float:
    q, t = bigrams(question), bigrams(title)
    return len(q & t) / len(t) if t else 0.0


def main() -> None:
    papers = [json.loads(l) for l in open(config.DATA / "papers.jsonl", encoding="utf-8")]
    src = config.DATA / "sources.json"
    if src.exists():                      # source papers fixed at collection time
        by_id = {p["id"]: p for p in papers}
        gold = [by_id[i] for i in json.loads(src.read_text()) if i in by_id][:config.N_QUESTIONS]
    else:
        gold = random.Random(config.SEED).sample(papers, config.N_QUESTIONS)
    kinds = list(TYPES)

    rows = []
    for i, p in enumerate(gold):
        kind = kinds[i % len(kinds)]
        user = (f"Title: {p['title']}\nAbstract: {p['abstract']}\n\n"
                f"Style: {TYPES[kind]}")
        text, _ = llm.complete(config.QUESTION_MODEL, SYSTEM, user, max_tokens=150)
        parsed = llm.extract_json(text) or {}
        q = str(parsed.get("question", "")).strip()
        if not q:
            print(f"  skipped {p['id']}: no question parsed")
            continue
        rows.append({"qid": f"q{i:03d}", "gold_id": p["id"], "type": kind, "question": q,
                     "title_overlap": round(overlap(q, p["title"]), 2),
                     "gold_title": p["title"]})
        print(f"{rows[-1]['qid']} [{kind}] {q}")

    with open(config.DATA / "questions.jsonl", "w", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps(r) + "\n")
    with open(config.DATA / "questions_review.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["qid", "type", "question", "gold_title", "title_overlap",
                    "ok (1/0)", "other_papers_that_also_answer", "notes"])
        for r in rows:
            w.writerow([r["qid"], r["type"], r["question"], r["gold_title"],
                        r["title_overlap"], "", "", ""])
    print(f"\nwrote {len(rows)} questions. spend so far: ${llm.LEDGER.usd:.4f}")


if __name__ == "__main__":
    main()
