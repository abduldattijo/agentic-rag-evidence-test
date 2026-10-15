"""Step 3: run every design on every question and log one row per (question, design).

    python run_eval.py                           # all four designs, all reviewed questions
    python run_eval.py --designs dense,rerank    # only the free (no LLM) designs
    python run_eval.py --limit 5                 # smoke test on 5 questions

Safe to stop and restart: finished (question, design) pairs are skipped.
"""
from __future__ import annotations

import argparse
import csv
import json
import time

import config
import llm
import metrics
from retrievers import DESIGNS, Corpus


def load_questions() -> list:
    qs = [json.loads(l) for l in open(config.DATA / "questions.jsonl", encoding="utf-8")]
    review = config.DATA / "questions_review.csv"
    if review.exists():
        ok = {}
        for row in csv.DictReader(open(review, encoding="utf-8")):
            ok[row["qid"]] = row.get("ok (1/0)", "").strip()
        kept = [q for q in qs if ok.get(q["qid"]) == "1"]
        if not kept:
            raise SystemExit("No question is marked 1 in questions_review.csv yet. "
                             "Review the questions first (PLAN.md, step 3).")
        print(f"{len(kept)} of {len(qs)} questions passed your review")
        return kept
    return qs


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--designs", default="dense,multiquery,rerank,agent")
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--out", default=str(config.RESULTS / f"{config.MODE}.jsonl"))
    args = ap.parse_args()

    config.RESULTS.mkdir(exist_ok=True)
    papers = [json.loads(l) for l in open(config.DATA / "papers.jsonl", encoding="utf-8")]
    corpus = Corpus(papers)
    questions = load_questions()
    if args.limit:
        questions = questions[:args.limit]

    names = [d.strip() for d in args.designs.split(",")]
    retrievers = {n: DESIGNS[n](corpus) for n in names}

    done = set()
    try:
        for line in open(args.out, encoding="utf-8"):
            r = json.loads(line)
            done.add((r["qid"], r["design"]))
    except FileNotFoundError:
        pass

    t_start = time.time()
    with open(args.out, "a", encoding="utf-8") as out:
        for i, q in enumerate(questions, start=1):
            for n in names:
                if (q["qid"], n) in done:
                    continue
                res = retrievers[n].retrieve(q["question"])
                row = {
                    "qid": q["qid"], "design": n, "type": q["type"], "gold_id": q["gold_id"],
                    "ranked": res.ranked_ids,
                    "hit_at_5": metrics.recall_at_k(res.ranked_ids, q["gold_id"], config.K_FINAL),
                    "rr": metrics.reciprocal_rank(res.ranked_ids, q["gold_id"], config.RANK_DEPTH),
                    "searches": res.searches, "llm_in": res.llm_in, "llm_out": res.llm_out,
                    "usd": res.usd, "latency_s": round(res.latency_s, 3), "trace": res.trace,
                }
                out.write(json.dumps(row) + "\n")
                out.flush()
            print(f"[{i}/{len(questions)}] spend ${llm.LEDGER.usd:.4f}  "
                  f"elapsed {time.time() - t_start:.0f}s", flush=True)
    print(f"done. results in {args.out}. total LLM spend this run: ${llm.LEDGER.usd:.4f}")


if __name__ == "__main__":
    main()
