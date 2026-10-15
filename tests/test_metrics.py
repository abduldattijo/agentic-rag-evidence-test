"""Run with: python3 tests/test_metrics.py   (standard library only)"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import metrics
from retrievers import rrf


def test_recall_and_rr():
    ranked = ["a", "b", "c", "d", "e", "f"]
    assert metrics.recall_at_k(ranked, "c", 5) == 1.0
    assert metrics.recall_at_k(ranked, "f", 5) == 0.0
    assert metrics.recall_at_k(ranked, "zzz", 5) == 0.0
    assert metrics.reciprocal_rank(ranked, "a") == 1.0
    assert metrics.reciprocal_rank(ranked, "d") == 0.25
    assert metrics.reciprocal_rank(ranked, "zzz") == 0.0


def test_bootstrap_range_contains_mean_and_is_ordered():
    vals = [1.0] * 30 + [0.0] * 70
    m, lo, hi = metrics.bootstrap_ci(vals, n_boot=500, seed=1)
    assert abs(m - 0.3) < 1e-9
    assert lo <= m <= hi
    assert 0.15 < lo and hi < 0.45


def test_paired_diff_sign():
    a = [1.0, 1.0, 0.0, 1.0]
    b = [0.0, 1.0, 0.0, 0.0]
    m, lo, hi = metrics.paired_diff_ci(a, b, n_boot=300, seed=2)
    assert abs(m - 0.5) < 1e-9


def test_cost_per_correct():
    assert metrics.cost_per_correct(2.0, 4) == 0.5
    assert metrics.cost_per_correct(2.0, 0) == float("inf")


def test_rrf_prefers_documents_ranked_well_in_several_lists():
    fused = rrf([["a", "b", "c"], ["b", "a", "d"], ["b", "c", "a"]])
    assert fused[0] == "b"
    assert set(fused) == {"a", "b", "c", "d"}


if __name__ == "__main__":
    for name, fn in list(globals().items()):
        if name.startswith("test_"):
            fn()
            print("ok ", name)
