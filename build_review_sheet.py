"""Writes data_<mode>/review_work.txt: each question, its source abstract, and the 3 closest OTHER
papers by embedding similarity, so a reviewer can check for an equally good answer.
Does not look at which design finds the source paper."""
import csv, json, numpy as np, config
from retrievers import Corpus

rows = list(csv.reader(open(config.DATA / "questions_review.csv", encoding="utf-8")))
head, body = rows[0], sorted(rows[1:], key=lambda r: r[0])
csv.writer(open(config.DATA / "questions_review.csv", "w", newline="", encoding="utf-8")).writerows([head] + body)
P = [json.loads(l) for l in open(config.DATA / "papers.jsonl", encoding="utf-8")]
by = {p["id"]: p for p in P}
Q = {json.loads(l)["qid"]: json.loads(l) for l in open(config.DATA / "questions.jsonl", encoding="utf-8")}
c = Corpus(P)
E = c.embeddings()
S = c._model().encode([Q[r[0]]["question"] for r in body], normalize_embeddings=True, batch_size=32) @ E.T
with open(config.DATA / "review_work.txt", "w", encoding="utf-8") as out:
    for i, r in enumerate(body):
        q = Q[r[0]]; g = by[q["gold_id"]]
        alts = [j for j in np.argsort(-S[i]) if P[j]["id"] != g["id"]][:3]
        out.write(f"### {q['qid']} [{q['type']}] id={g['id']}\nQ: {q['question']}\nGOLD: {g['title']}\n  {g['abstract']}\n")
        for j in alts:
            o = P[j]
            out.write(f"  ALT {o['id']}: {o['title']} :: {' '.join(o['abstract'].split()[:40])}...\n")
        out.write("\n")
print(len(body), "rows written")
