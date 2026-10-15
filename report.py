"""Step 4: turn results/<mode>.jsonl into the tables the article needs.

    python report.py                   # uses results/<MODE>.jsonl
    python report.py results/full.jsonl

Prints (1) the main table with 95% bootstrap ranges, (2) each design against `dense` on the
same questions, (3) questions where a design did WORSE than `dense`, and (4) agent misses after
the maximum number of searches. Numbers only; the write-up must follow what these say.
"""
from __future__ import annotations

import json
import statistics
import sys
from collections import defaultdict

import config
import metrics


def main() -> None:
    path = sys.argv[1] if len(sys.argv) > 1 else str(config.RESULTS / f"{config.MODE}.jsonl")
    rows = [json.loads(l) for l in open(path, encoding="utf-8")]
    by_design = defaultdict(dict)
    for r in rows:
        by_design[r["design"]][r["qid"]] = r

    # use only questions every design answered, so every column is on the same questions
    common = set.intersection(*[set(d) for d in by_design.values()])
    qids = sorted(common)
    print(f"{len(qids)} questions answered by all {len(by_design)} designs ({path})\n")

    print(f"{'design':<11}{'recall@5 [95% range]':<26}{'MRR@10 [95% range]':<26}"
          f"{'median s':>9}{'tok in':>9}{'tok out':>9}{'searches':>9}{'$/query':>10}{'$/correct':>11}")
    for name, d in by_design.items():
        rs = [d[q] for q in qids]
        rec = metrics.bootstrap_ci([r["hit_at_5"] for r in rs])
        mrr = metrics.bootstrap_ci([r["rr"] for r in rs])
        usd = sum(r["usd"] for r in rs)
        hits = sum(r["hit_at_5"] for r in rs)
        cpc = metrics.cost_per_correct(usd, hits)
        print(f"{name:<11}{rec[0]:.3f} [{rec[1]:.3f}, {rec[2]:.3f}]".ljust(37) +
              f"{mrr[0]:.3f} [{mrr[1]:.3f}, {mrr[2]:.3f}]".ljust(26) +
              f"{statistics.median(r['latency_s'] for r in rs):>9.2f}"
              f"{statistics.mean(r['llm_in'] for r in rs):>9.0f}"
              f"{statistics.mean(r['llm_out'] for r in rs):>9.0f}"
              f"{statistics.mean(r['searches'] for r in rs):>9.1f}"
              f"{usd / len(rs):>10.5f}"
              f"{('free' if usd == 0 else f'{cpc:.5f}'):>11}")

    if "dense" in by_design:
        print("\nDifference in recall@5 vs dense, same questions (positive = better than dense):")
        base = [by_design["dense"][q]["hit_at_5"] for q in qids]
        for name, d in by_design.items():
            if name == "dense":
                continue
            diff = metrics.paired_diff_ci([d[q]["hit_at_5"] for q in qids], base)
            verdict = ("range excludes 0" if diff[1] > 0 or diff[2] < 0 else "range includes 0: not clear")
            print(f"  {name:<11}{diff[0]:+.3f}  [{diff[1]:+.3f}, {diff[2]:+.3f}]  {verdict}")

        print("\nQuestions where a design lost a paper that dense had in its top 5 (read these):")
        for name, d in by_design.items():
            if name == "dense":
                continue
            hurt = [q for q in qids
                    if by_design["dense"][q]["hit_at_5"] == 1 and d[q]["hit_at_5"] == 0]
            print(f"  {name}: {len(hurt)} of {len(qids)}  {hurt[:10]}")

    if "agent" in by_design:
        miss = [q for q in qids
                if by_design["agent"][q]["hit_at_5"] == 0
                and by_design["agent"][q]["searches"] >= config.AGENT_MAX_SEARCHES]
        print(f"\nAgent used all {config.AGENT_MAX_SEARCHES} searches and still missed: "
              f"{len(miss)} of {len(qids)} questions ({100 * len(miss) / len(qids):.0f}%)")
        print(f"  {miss[:10]}")

    print("\nBy question type, recall@5:")
    types = sorted({r["type"] for r in rows})
    for t in types:
        line = f"  {t:<9}"
        for name, d in by_design.items():
            sel = [d[q]["hit_at_5"] for q in qids if d[q]["type"] == t]
            line += f"  {name} {metrics.mean(sel):.2f} (n={len(sel)})"
        print(line)


if __name__ == "__main__":
    main()
