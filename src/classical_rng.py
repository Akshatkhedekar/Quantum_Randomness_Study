"""
Classical Random Number Generator
Uses NumPy's PCG64 (Permuted Congruential Generator)
"""

import numpy as np


def generate_random_numbers(total_numbers=10000, seed=None):
    """
    Generate classical random numbers using PCG64.

    Range: 0 to 255 (like a byte)

    Args:
        total_numbers: Number of random numbers to generate (default: 10000)
        seed: Optional seed for reproducibility.
              Same seed always produces the same sequence.
              If None, uses OS entropy (non-reproducible).

    Returns:
        List of random integers in range [0, 255]
    """
    rng = np.random.default_rng(seed)
    return rng.integers(0, 256, size=total_numbers).tolist()
