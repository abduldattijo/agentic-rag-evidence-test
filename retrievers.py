"""The four retrieval designs. All share one corpus, one embedder and one interface:

    retriever.retrieve(question) -> Result(ranked_ids=[...], searches, tokens, usd, latency)

dense       one search with the original question                         (baseline)
multiquery  LLM writes N rewrites, search each, fuse with reciprocal-rank fusion
rerank      dense top-50, then a cross-encoder reorders them
agent       first search is the original question (same as `dense`); then an LLM looks at what
            came back and either stops or writes a new query, up to AGENT_MAX_SEARCHES total.
            Final ranking = the searches fused by rank (RRF, same setting as multiquery).
"""
from __future__ import annotations

import hashlib
import time
from dataclasses import dataclass, field
from typing import Dict, List, Tuple

import config
import llm


@dataclass
class Result:
    ranked_ids: List[str]
    searches: int = 1
    llm_in: int = 0
    llm_out: int = 0
    usd: float = 0.0
    latency_s: float = 0.0
    trace: list = field(default_factory=list)


class Corpus:
    def __init__(self, papers: List[dict]):
        self.papers = papers
        self.ids = [p["id"] for p in papers]
        self.title = {p["id"]: p["title"] for p in papers}
        self.texts = [f'{p["title"]}. {p["abstract"]}' for p in papers]
        self._emb = None
        self._embedder = None

    def _model(self):
        if self._embedder is None:
            from sentence_transformers import SentenceTransformer
            self._embedder = SentenceTransformer(config.EMBED_MODEL, device="cpu")  # MPS ran out of memory at 2000 papers
        return self._embedder

    def embeddings(self):
        import numpy as np
        if self._emb is None:
            key = hashlib.md5(("|".join(self.ids) + config.EMBED_MODEL).encode()).hexdigest()[:12]
            path = config.DATA / f"emb_{key}.npy"
            if path.exists():
                self._emb = np.load(path)
            else:
                self._emb = self._model().encode(self.texts, normalize_embeddings=True,
                                                 batch_size=64, show_progress_bar=True)
                np.save(path, self._emb)
        return self._emb

    def search(self, query: str, k: int) -> List[Tuple[str, float]]:
        import numpy as np
        q = self._model().encode([query], normalize_embeddings=True)[0]
        scores = self.embeddings() @ q
        top = np.argsort(-scores)[:k]
        return [(self.ids[i], float(scores[i])) for i in top]


def rrf(rankings: List[List[str]], k: int = config.RRF_K) -> List[str]:
    """Reciprocal-rank fusion of several ranked id lists."""
    score: Dict[str, float] = {}
    for ranking in rankings:
        for rank, doc in enumerate(ranking, start=1):
            score[doc] = score.get(doc, 0.0) + 1.0 / (k + rank)
    return [d for d, _ in sorted(score.items(), key=lambda t: -t[1])]


def _add(res: Result, usage: dict) -> None:
    res.llm_in += usage["in"]
    res.llm_out += usage["out"]
    res.usd += usage["usd"]


class Dense:
    name = "dense"

    def __init__(self, corpus: Corpus):
        self.c = corpus

    def retrieve(self, question: str) -> Result:
        t0 = time.time()
        hits = self.c.search(question, config.RANK_DEPTH)
        return Result([d for d, _ in hits], searches=1, latency_s=time.time() - t0)


class MultiQuery:
    name = "multiquery"

    def __init__(self, corpus: Corpus):
        self.c = corpus

    def retrieve(self, question: str) -> Result:
        t0 = time.time()
        res = Result([], searches=0)
        system = ("You write search queries for a database of recent AI research paper abstracts. "
                  "Reply with only a JSON list of strings.")
        user = (f"Question: {question}\n\nWrite {config.MULTI_QUERY_N} different search queries "
                "that could find the paper that answers it. Vary the wording and the angle.")
        text, usage = llm.complete(config.AGENT_MODEL, system, user, max_tokens=300)
        _add(res, usage)
        parsed = llm.extract_json(text)
        queries = [question] + [q for q in (parsed or []) if isinstance(q, str)][:config.MULTI_QUERY_N]
        rankings = []
        for q in queries:
            rankings.append([d for d, _ in self.c.search(q, config.RERANK_CANDIDATES)])
            res.searches += 1
        res.ranked_ids = rrf(rankings)[:config.RANK_DEPTH]
        res.trace = queries
        res.latency_s = time.time() - t0
        return res


class Rerank:
    name = "rerank"

    def __init__(self, corpus: Corpus):
        self.c = corpus
        self._ce = None

    def retrieve(self, question: str) -> Result:
        t0 = time.time()
        if self._ce is None:
            from sentence_transformers import CrossEncoder
            self._ce = CrossEncoder(config.RERANK_MODEL, device="cpu")
        cands = [d for d, _ in self.c.search(question, config.RERANK_CANDIDATES)]
        index = {d: i for i, d in enumerate(self.c.ids)}
        pairs = [(question, self.c.texts[index[d]]) for d in cands]
        scores = self._ce.predict(pairs)
        order = sorted(zip(cands, scores), key=lambda t: -t[1])
        return Result([d for d, _ in order][:config.RANK_DEPTH], searches=1,
                      latency_s=time.time() - t0)


class Agent:
    name = "agent"

    def __init__(self, corpus: Corpus):
        self.c = corpus

    def retrieve(self, question: str) -> Result:
        t0 = time.time()
        res = Result([], searches=0)
        rankings: List[List[str]] = []      # one ranked id list per search, fused with RRF at the end
        history: List[str] = []

        query = question
        while res.searches < config.AGENT_MAX_SEARCHES:
            hits = self.c.search(query, config.RERANK_CANDIDATES)   # same depth as multiquery
            res.searches += 1
            rankings.append([d for d, _ in hits])
            shown = hits[:config.K_FINAL]                    # the model sees the top 5 titles
            history.append(f'Search {res.searches}: "{query}"\n' +
                           "\n".join(f"  - {self.c.title[d]}" for d, _ in shown))
            res.trace.append({"query": query, "top": [d for d, _ in hits[:config.RANK_DEPTH]]})
            if res.searches >= config.AGENT_MAX_SEARCHES:
                break
            system = ("You are a research assistant finding the single arXiv paper that answers a "
                      "question. After each search decide whether the results contain it. "
                      'Reply with only JSON: {"decision": "stop"} or '
                      '{"decision": "search", "query": "<a new, different query>"}.')
            user = f"Question: {question}\n\n" + "\n\n".join(history)
            text, usage = llm.complete(config.AGENT_MODEL, system, user, max_tokens=150)
            _add(res, usage)
            parsed = llm.extract_json(text) or {}
            nxt = parsed.get("query") if parsed.get("decision") == "search" else None
            if not isinstance(nxt, str) or not nxt.strip() or nxt.strip() == query:
                break
            query = nxt.strip()

        # Scores from different queries are not comparable (pilot q005: a rewrite pushed the right
        # paper from rank 1 to rank 4 under a best-score merge), so searches are fused by rank,
        # with the same RRF setting as multiquery.
        res.ranked_ids = rrf(rankings)[:config.RANK_DEPTH]
        res.latency_s = time.time() - t0
        return res


DESIGNS = {cls.name: cls for cls in (Dense, MultiQuery, Rerank, Agent)}
