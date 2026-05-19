"""
Data Handler for Random Number Generation Results
Handles saving and loading random number data in CSV format.
"""

import os

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")
CLASSICAL_FILE = os.path.join(DATA_DIR, "classical.csv")
QUANTUM_FILE = os.path.join(DATA_DIR, "quantum.csv")


def save_data(classical, quantum):
    """
    Save classical and quantum random numbers to CSV files.
    Overwrites existing files each run.

    Args:
        classical: List of classical random numbers
        quantum: List of quantum random numbers
    """
    os.makedirs(DATA_DIR, exist_ok=True)

    with open(CLASSICAL_FILE, "w") as f:
        for num in classical:
            f.write(str(num) + "\n")

    with open(QUANTUM_FILE, "w") as f:
        for num in quantum:
            f.write(str(num) + "\n")


def load_data():
    """
    Load classical and quantum random numbers from CSV files.

    Returns:
        Tuple of (classical_numbers, quantum_numbers) as lists.
        Returns empty lists if files don't exist.
    """
    def _load_file(filepath):
        if not os.path.exists(filepath):
            return []
        with open(filepath, "r") as f:
            return [int(line.strip()) for line in f if line.strip()]

    classical = _load_file(CLASSICAL_FILE)
    quantum = _load_file(QUANTUM_FILE)
    return classical, quantum
