"""Summary of the frozen full benchmark: dense and rerank (one run each, deterministic) and the
LLM designs multiquery and agent (three runs each).

    MODE=full python summarize_runs.py
"""
from __future__ import annotations

import glob
import json
import statistics as st
from collections import defaultdict

import config
import metrics


def load(path):
    return [json.loads(l) for l in open(path, encoding="utf-8")]


def by_design(rows):
    d = defaultdict(dict)
    for r in rows:
        d[r["design"]][r["qid"]] = r
    return d


def main() -> None:
    base = by_design(load(config.RESULTS / "full.jsonl"))
    runs = [by_design(load(p)) for p in sorted(glob.glob(str(config.RESULTS / "full_run[0-9].jsonl")))]
    qids = sorted(base["dense"])
    for n in ("multiquery", "agent"):
        for r in runs:
            qids = [q for q in qids if q in r[n]]
    print(f"{len(qids)} questions, {len(runs)} LLM runs\n")

    def arr(d, key):  # per-question values in qid order
        return [d[q][key] for q in qids]

    table = {}
    table["dense"] = [base["dense"]]
    table["rerank"] = [base["rerank"]]
    table["multiquery"] = [r["multiquery"] for r in runs]
    table["agent"] = [r["agent"] for r in runs]

    print(f"{'design':11s} {'recall@5 mean [min-max over runs]':38s} {'MRR@10 mean [min-max]':26s} "
          f"{'searches':>8s} {'median s':>8s} {'$/query':>9s} {'$/correct':>10s}")
    for n, rs in table.items():
        rec = [metrics.mean(arr(r, "hit_at_5")) for r in rs]
        mrr = [metrics.mean(arr(r, "rr")) for r in rs]
        lat = [st.median(arr(r, "latency_s")) for r in rs]
        usd = [metrics.mean(arr(r, "usd")) for r in rs]
        sea = [metrics.mean(arr(r, "searches")) for r in rs]
        corr = [u * len(qids) / (rc * len(qids)) if rc else float("inf") for u, rc in zip(usd, rec)]
        rng = lambda v, f="{:.3f}": f"{f.format(metrics.mean(v))} [{f.format(min(v))}-{f.format(max(v))}]"
        print(f"{n:11s} {rng(rec):38s} {rng(mrr):26s} {metrics.mean(sea):8.1f} {metrics.mean(lat):8.2f} "
              f"{metrics.mean(usd):9.5f} {('free' if metrics.mean(usd)==0 else '%.5f' % metrics.mean(corr)):>10s}")

    print("\nPaired difference vs dense (positive = better than dense), same questions")
    dn = arr(base["dense"], "hit_at_5"), arr(base["dense"], "rr")
    for n in ("rerank", "multiquery", "agent"):
        for label, idx, key in (("recall@5", 0, "hit_at_5"), ("MRR@10", 1, "rr")):
            per_run = []
            for i, r in enumerate(table[n], start=1):
                m, lo, hi = metrics.paired_diff_ci(arr(r, key), dn[idx])
                per_run.append((m, lo, hi))
            avg = [metrics.mean([arr(r, key)[j] for r in table[n]]) for j in range(len(qids))]
            m, lo, hi = metrics.paired_diff_ci(avg, dn[idx])
            runs_txt = "  ".join(f"run{i}: {a:+.3f} [{b:+.3f},{c:+.3f}]" for i, (a, b, c) in enumerate(per_run, 1)) \
                if len(per_run) > 1 else ""
            verdict = "includes 0: no clear difference" if lo <= 0 <= hi else ("better" if m > 0 else "worse")
            print(f"  {n:10s} {label:9s} mean over runs {m:+.3f} [{lo:+.3f}, {hi:+.3f}] {verdict}")
            if runs_txt:
                print(f"             {runs_txt}")

    print("\nQuestions dense missed in the top 5 (n = %d):" % int(sum(1 for q in qids if not base['dense'][q]['hit_at_5'])))
    for n in ("rerank", "multiquery", "agent"):
        rescued = [sum(1 for q in qids if not base["dense"][q]["hit_at_5"] and r[q]["hit_at_5"]) for r in table[n]]
        lost = [sum(1 for q in qids if base["dense"][q]["hit_at_5"] and not r[q]["hit_at_5"]) for r in table[n]]
        print(f"  {n:10s} rescued per run {rescued}   lost a dense hit per run {lost}")
    ag = table["agent"]
    stop = [metrics.mean([1.0 if r[q]["searches"] == 1 else 0.0 for q in qids]) for r in ag]
    full = [metrics.mean([1.0 if r[q]["searches"] >= config.AGENT_MAX_SEARCHES else 0.0 for q in qids]) for r in ag]
    print(f"\nAgent stopped after one search: {[round(x, 2) for x in stop]} of questions per run")
    print(f"Agent used all {config.AGENT_MAX_SEARCHES} searches: {[round(x, 2) for x in full]}")
    miss_full = [sum(1 for q in qids if r[q]["searches"] >= config.AGENT_MAX_SEARCHES and not r[q]["hit_at_5"]) for r in ag]
    print(f"...and still missed: {miss_full} questions per run")


if __name__ == "__main__":
    main()
