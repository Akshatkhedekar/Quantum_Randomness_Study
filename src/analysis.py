"""
Analysis module for random number data.
Provides basic statistical analysis and comparison.
"""

import numpy as np
from scipy import stats


def basic_stats(data):
    """
    Compute basic statistical measures for a dataset.

    Args:
        data: List or array of numbers

    Returns:
        Dictionary with mean, variance, standard_deviation, min, max
    """
    arr = np.array(data)
    return {
        "mean": float(np.mean(arr)),
        "variance": float(np.var(arr)),
        "standard_deviation": float(np.std(arr)),
        "min": int(np.min(arr)),
        "max": int(np.max(arr)),
    }


def uniformity_check(data, bins=10):
    """
    Check how evenly data is distributed across the 0-255 range.

    Divides the range into equal-width bins and counts numbers in each.

    Args:
        data: List or array of numbers
        bins: Number of equal-width bins (default: 10)

    Returns:
        List of counts, one per bin
    """
    counts, _ = np.histogram(data, bins=bins, range=(0, 256))
    return counts.tolist()


def compare_datasets(classical, quantum):
    """
    Compare classical and quantum random datasets.

    Computes basic_stats for both and returns a structured dictionary.

    Args:
        classical: List of classical random numbers
        quantum: List of quantum random numbers

    Returns:
        Dictionary with "classical" and "quantum" keys containing stats
    """
    return {
        "classical": basic_stats(classical),
        "quantum": basic_stats(quantum),
    }


def ks_test(classical, quantum):
    """
    Two-sample Kolmogorov-Smirnov test.

    Compares the distributions of two datasets.
    Low p-value (< 0.05) suggests different distributions.

    Args:
        classical: List of classical random numbers
        quantum: List of quantum random numbers

    Returns:
        Dictionary with "statistic", "p_value", and "interpretation"
    """
    statistic, p_value = stats.ks_2samp(classical, quantum)
    interpretation = (
        "No statistically significant difference between distributions"
        if p_value > 0.05
        else "Significant difference detected"
    )
    return {
        "statistic": float(statistic),
        "p_value": float(p_value),
        "interpretation": interpretation,
    }


def calculate_entropy(data, bins=20):
    """
    Calculate Shannon entropy of the dataset.

    Creates a histogram, normalizes to probabilities,
    then computes entropy. Higher entropy = more randomness.

    Args:
        data: List or array of numbers
        bins: Number of bins for histogram (default: 20)

    Returns:
        Dictionary with "value" (entropy as float)
    """
    counts, _ = np.histogram(data, bins=bins, range=(0, 256))
    probabilities = counts / np.sum(counts)
    entropy = stats.entropy(probabilities)
    return {"value": float(entropy)}


def autocorrelation(data, lag=1):
    """
    Compute autocorrelation at a given lag.

    Measures relationship between values and their
    lag-shifted copies. Near 0 = more independent.

    Args:
        data: List or array of numbers
        lag: Time shift (default: 1)

    Returns:
        Dictionary with "value" and "interpretation"
    """
    arr = np.array(data)
    corr_matrix = np.corrcoef(arr[:-lag], arr[lag:])
    corr = float(corr_matrix[0, 1])
    interpretation = (
        "No significant autocorrelation (values appear independent)"
        if abs(corr) < 0.05
        else "Some correlation detected (possible pattern)"
    )
    return {
        "value": corr,
        "interpretation": interpretation,
    }


def full_analysis(classical, quantum):
    """
    Run all advanced tests on both datasets.

    Calls ks_test, calculate_entropy, and autocorrelation
    for both classical and quantum data. Includes a comparison
    of entropy values between the two.

    Args:
        classical: List of classical random numbers
        quantum: List of quantum random numbers

    Returns:
        Dictionary with "ks_test", "entropy", and "autocorrelation" keys
    """
    classical_entropy = calculate_entropy(classical)["value"]
    quantum_entropy = calculate_entropy(quantum)["value"]
    if abs(quantum_entropy - classical_entropy) < 0.01:
        entropy_interpretation = "Both datasets show similar randomness levels"
    elif quantum_entropy > classical_entropy:
        entropy_interpretation = "Quantum shows higher randomness"
    else:
        entropy_interpretation = "Classical shows higher randomness"
    return {
        "ks_test": ks_test(classical, quantum),
        "entropy": {
            "classical": classical_entropy,
            "quantum": quantum_entropy,
            "interpretation": entropy_interpretation,
        },
        "autocorrelation": {
            "classical": autocorrelation(classical),
            "quantum": autocorrelation(quantum),
        },
    }


def determinism_demo():
    """
    Demonstrate that classical RNG is deterministic (seedable)
    while quantum RNG is non-deterministic.

    Classical with the same seed produces identical sequences.
    Quantum produces different sequences every run.

    Returns:
        Dictionary with classical and quantum comparison results
    """
    from src.classical_rng import generate_random_numbers
    from src.quantum_rng import generate_quantum_numbers

    c1 = generate_random_numbers(100, seed=42)
    c2 = generate_random_numbers(100, seed=42)

    q1 = generate_quantum_numbers(100)
    q2 = generate_quantum_numbers(100)

    return {
        "classical": {
            "identical": c1 == c2,
            "first_five": c1[:5],
            "second_five": c2[:5],
        },
        "quantum": {
            "different": q1 != q2,
            "first_five": q1[:5],
            "second_five": q2[:5],
        },
    }


def determinism_explanation():
    """
    Return explanation of why determinism matters for security.

    Returns:
        Dictionary with explanation text
    """
    return {
        "explanation": (
            "Both generators pass basic randomness tests, "
            "but only classical can be fully reproduced with a known seed. "
            "This means classical PRNGs depend on seed secrecy, "
            "and predictability becomes possible if the seed is known."
        ),
    }
