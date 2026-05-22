import numpy as np
from src.analysis import (
    basic_stats,
    uniformity_check,
    compare_datasets,
    ks_test,
    calculate_entropy,
    autocorrelation,
    full_analysis,
    determinism_demo,
    determinism_explanation,
)


def test_basic_stats():
    data = [0, 128, 255]
    stats = basic_stats(data)
    assert stats["mean"] == 127.66666666666667
    assert stats["min"] == 0
    assert stats["max"] == 255
    assert "variance" in stats
    assert "standard_deviation" in stats


def test_uniformity_check():
    data = list(range(256))
    counts = uniformity_check(data, bins=4)
    assert len(counts) == 4
    assert all(c == 64 for c in counts)


def test_compare_datasets():
    c = [1, 2, 3]
    q = [4, 5, 6]
    result = compare_datasets(c, q)
    assert "classical" in result
    assert "quantum" in result
    assert result["classical"]["mean"] == 2.0
    assert result["quantum"]["mean"] == 5.0


def test_ks_test_identical():
    data = list(range(100))
    result = ks_test(data, data)
    assert result["p_value"] == 1.0
    assert "No statistically significant difference" in result["interpretation"]


def test_ks_test_different():
    a = [0] * 100
    b = [255] * 100
    result = ks_test(a, b)
    assert result["p_value"] < 0.05
    assert "Significant difference" in result["interpretation"]


def test_calculate_entropy():
    rng = np.random.default_rng(42)
    data = rng.integers(0, 256, size=10000).tolist()
    entropy = calculate_entropy(data, bins=20)
    assert entropy["value"] > 2.5


def test_autocorrelation_no_pattern():
    rng = np.random.default_rng(42)
    data = rng.integers(0, 256, size=1000).tolist()
    result = autocorrelation(data, lag=1)
    assert abs(result["value"]) < 0.15


def test_autocorrelation_pattern():
    data = [0, 255] * 50
    result = autocorrelation(data, lag=1)
    assert result["value"] < -0.95


def test_full_analysis_structure():
    a = [1, 2, 3, 4, 5]
    b = [6, 7, 8, 9, 10]
    result = full_analysis(a, b)
    assert "ks_test" in result
    assert "entropy" in result
    assert "autocorrelation" in result
    assert "classical" in result["entropy"]
    assert "quantum" in result["entropy"]


def test_determinism_demo():
    result = determinism_demo()
    assert result["classical"]["identical"] is True
    assert result["quantum"]["different"] is True


def test_determinism_explanation():
    result = determinism_explanation()
    assert "explanation" in result
    assert len(result["explanation"]) > 0
