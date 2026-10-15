"""Writes results/rescued_and_lost_examples.md: every question where the agent rescued a dense
miss, lost a dense hit, or never found the paper, with the agent's queries from all 3 runs.

    MODE=full python export_examples.py
"""
import glob
import json

import config

P = {json.loads(l)["id"]: json.loads(l) for l in open(config.DATA / "papers.jsonl", encoding="utf-8")}
Q = {json.loads(l)["qid"]: json.loads(l) for l in open(config.DATA / "questions.jsonl", encoding="utf-8")}
dense = {}
for l in open(config.RESULTS / "full.jsonl", encoding="utf-8"):
    r = json.loads(l)
    if r["design"] == "dense":
        dense[r["qid"]] = r
runs = []
for p in sorted(glob.glob(str(config.RESULTS / "full_run[0-9].jsonl"))):
    d = {}
    for l in open(p, encoding="utf-8"):
        r = json.loads(l)
        if r["design"] == "agent":
            d[r["qid"]] = r
    runs.append(d)
qids = [q for q in dense if all(q in r for r in runs)]


def rank(r, g):
    return r["ranked"].index(g) + 1 if g in r["ranked"] else None


groups = {"Rescued (dense missed the top 5, agent found it in at least one run)": [],
          "Lost (dense had it in the top 5, agent missed it in at least one run)": [],
          "Never found (dense and all 3 agent runs missed the top 5)": []}
keys = list(groups)
for q in qids:
    dh = dense[q]["hit_at_5"]
    ah = [r[q]["hit_at_5"] for r in runs]
    if not dh and any(ah):
        groups[keys[0]].append(q)
    if dh and not all(ah):
        groups[keys[1]].append(q)
    if not dh and not any(ah):
        groups[keys[2]].append(q)

out = ["# Agent vs dense: rescued, lost and never-found questions",
       "",
       f"Frozen question set ({len(qids)} questions), agent run 3 times. Ranks are the position of the "
       "correct paper in the top 10 (`-` = not in top 10). Queries are exactly what the agent wrote.",
       "",
       "Counts: " + ", ".join(f"{k.split(' (')[0]} {len(v)}" for k, v in groups.items()), ""]
for title, ids in groups.items():
    out += [f"## {title}", ""]
    for q in ids:
        g = Q[q]["gold_id"]
        dr = rank(dense[q], g)
        out += [f"### {q} ({Q[q]['type']})",
                f"**Question:** {Q[q]['question']}",
                f"**Correct paper:** {P[g]['title']} ({g})",
                f"**Dense rank:** {dr or '-'}   **Agent ranks, runs 1-3:** "
                + ", ".join(str(rank(r[q], g) or "-") for r in runs)
                + f"   **Searches:** " + ", ".join(str(r[q]["searches"]) for r in runs), ""]
        for i, r in enumerate(runs, start=1):
            out.append(f"- Run {i}:")
            for t in r[q]["trace"]:
                top3 = "; ".join(P[x]["title"][:60] for x in t["top"][:3])
                out.append(f"  - query: {t['query']}")
                out.append(f"    - correct paper in top 10: {'yes' if g in t['top'] else 'no'}; top 3: {top3}")
        out.append("")
(config.RESULTS / "rescued_and_lost_examples.md").write_text("\n".join(out), encoding="utf-8")
print("wrote", config.RESULTS / "rescued_and_lost_examples.md", "-", {k.split(" (")[0]: len(v) for k, v in groups.items()})
