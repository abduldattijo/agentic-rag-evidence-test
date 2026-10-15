"""Retrieval metrics and confidence ranges. Standard library only, so it is easy to test."""
from __future__ import annotations

import random
from typing import List, Sequence, Tuple


def recall_at_k(ranked: Sequence[str], gold: str, k: int) -> float:
    """1.0 if the gold paper is in the top k, else 0.0 (one gold paper per question)."""
    return 1.0 if gold in list(ranked)[:k] else 0.0


def reciprocal_rank(ranked: Sequence[str], gold: str, depth: int = 10) -> float:
    for i, doc in enumerate(list(ranked)[:depth], start=1):
        if doc == gold:
            return 1.0 / i
    return 0.0


def mean(xs: Sequence[float]) -> float:
    return sum(xs) / len(xs) if xs else float("nan")


def bootstrap_ci(values: Sequence[float], n_boot: int = 2000, seed: int = 0,
                 alpha: float = 0.05) -> Tuple[float, float, float]:
    """(mean, low, high). Resamples questions with replacement."""
    vals = list(values)
    if not vals:
        return float("nan"), float("nan"), float("nan")
    rng = random.Random(seed)
    n = len(vals)
    means = sorted(mean([vals[rng.randrange(n)] for _ in range(n)]) for _ in range(n_boot))
    lo = means[int((alpha / 2) * n_boot)]
    hi = means[int((1 - alpha / 2) * n_boot) - 1]
    return mean(vals), lo, hi


def paired_diff_ci(a: Sequence[float], b: Sequence[float], n_boot: int = 2000,
                   seed: int = 0) -> Tuple[float, float, float]:
    """Mean of (a - b) over the same questions, with a bootstrap range."""
    if len(a) != len(b):
        raise ValueError("paired lists must have the same length")
    return bootstrap_ci([x - y for x, y in zip(a, b)], n_boot=n_boot, seed=seed)


def cost_per_correct(total_usd: float, hits: float) -> float:
    return total_usd / hits if hits else float("inf")
