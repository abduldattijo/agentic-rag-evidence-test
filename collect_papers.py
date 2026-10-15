"""Step 1: collect a random sample of recent arXiv papers (title + abstract) into data/papers.jsonl.

    python collect_papers.py

Uses the public arXiv API, which asks clients to wait 3 seconds between requests.
"""
from __future__ import annotations

import datetime as dt
import json
import math
import random
import re
from collections import Counter

import arxiv

import config


def stamp(day: str, end: bool) -> str:
    return day.replace("-", "") + ("2359" if end else "0000")


def date_windows(after: str, before: str, days: int):
    """[(start_day, end_day), ...] in `days`-day steps, so papers are spread over the whole period."""
    start = dt.date.fromisoformat(after)
    stop = dt.date.fromisoformat(before)
    out = []
    while start <= stop:
        end = min(start + dt.timedelta(days=days - 1), stop)
        out.append((start.isoformat(), end.isoformat()))
        start = end + dt.timedelta(days=1)
    return out


def tokens(p: dict) -> list:
    return re.findall(r"[a-z][a-z0-9]{2,}", (p["title"] + " " + p["abstract"]).lower())


def nearest(source: dict, pool: list, vectors: dict, k: int, taken: set) -> list:
    """The k pool papers most similar to `source` by TF-IDF cosine. TF-IDF, not the embedding
    model used for retrieval, so the choice of distractors does not favour the dense design."""
    q = vectors[source["id"]]
    scored = []
    for p in pool:
        if p["id"] == source["id"] or p["id"] in taken:
            continue
        v = vectors[p["id"]]
        small, big = (q, v) if len(q) < len(v) else (v, q)
        scored.append((sum(w * big.get(t, 0.0) for t, w in small.items()), p["id"]))
    scored.sort(reverse=True)
    return [pid for _, pid in scored[:k]]


def tfidf_vectors(pool: list) -> dict:
    df = Counter()
    for p in pool:
        df.update(set(tokens(p)))
    n = len(pool)
    out = {}
    for p in pool:
        tf = Counter(tokens(p))
        v = {t: (1 + math.log(c)) * math.log(n / df[t]) for t, c in tf.items()}
        norm = math.sqrt(sum(x * x for x in v.values())) or 1.0
        out[p["id"]] = {t: x / norm for t, x in v.items()}
    return out


def build_corpus(pool: list) -> tuple:
    """Pick source papers first (seeded), add close neighbours of each, fill with random papers."""
    rng = random.Random(config.SEED)
    rng.shuffle(pool)
    sources = pool[:config.N_QUESTIONS]
    chosen = {p["id"] for p in sources}
    corpus = list(sources)
    by_id = {p["id"]: p for p in pool}
    if config.DISTRACTORS_PER_SOURCE:
        vectors = tfidf_vectors(pool)
        for s in sources:
            for pid in nearest(s, pool, vectors, config.DISTRACTORS_PER_SOURCE, chosen):
                chosen.add(pid)
                corpus.append(by_id[pid])
    for p in pool:
        if len(corpus) >= config.CORPUS_SIZE:
            break
        if p["id"] not in chosen:
            chosen.add(p["id"])
            corpus.append(p)
    rng.shuffle(corpus)
    return corpus[:config.CORPUS_SIZE], [p["id"] for p in sources]


def main() -> None:
    config.DATA.mkdir(exist_ok=True)
    cats = " OR ".join(f"cat:{c}" for c in config.ARXIV_CATEGORIES)
    windows = date_windows(config.PUBLISHED_AFTER, config.PUBLISHED_BEFORE, config.WINDOW_DAYS)
    per_window = -(-config.CORPUS_SIZE * 3 // len(windows))     # about 3x what we need, per window
    client = arxiv.Client(page_size=100, delay_seconds=3.0, num_retries=3)

    seen, pool = set(), []
    for a, b in windows:
        query = f"({cats}) AND submittedDate:[{stamp(a, False)} TO {stamp(b, True)}]"
        search = arxiv.Search(query=query, max_results=per_window,
                              sort_by=arxiv.SortCriterion.SubmittedDate)
        got = 0
        for r in client.results(search):
            pid = re.sub(r"v\d+$", "", r.get_short_id())
            if pid in seen or len(r.summary.split()) < 40:      # duplicates and stub abstracts
                continue
            if r.primary_category not in config.ARXIV_CATEGORIES:  # keep AI/ML/NLP/IR papers
                continue
            seen.add(pid)
            pool.append({"id": pid, "title": " ".join(r.title.split()),
                         "abstract": " ".join(r.summary.split()),
                         "published": r.published.date().isoformat(),
                         "category": r.primary_category})
            got += 1
        if got:
            print(f"  {a} to {b}: {got} papers", flush=True)
    print(f"fetched {len(pool)} candidate papers")

    sample, source_ids = build_corpus(pool)
    out = config.DATA / "papers.jsonl"
    with open(out, "w", encoding="utf-8") as f:
        for p in sample:
            f.write(json.dumps(p) + "\n")
    # which papers the questions are written about; chosen before any retrieval is run
    (config.DATA / "sources.json").write_text(json.dumps(source_ids))
    print(f"wrote {len(sample)} papers to {out}; {len(source_ids)} source papers, "
          f"{config.DISTRACTORS_PER_SOURCE} close neighbours each")


if __name__ == "__main__":
    main()
