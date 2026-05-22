import os
import sys
import tempfile
import pytest

import numpy as np


PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

import matplotlib
matplotlib.use("Agg")


@pytest.fixture
def sample_classical():
    rng = np.random.default_rng(42)
    return rng.integers(0, 256, size=10).tolist()


@pytest.fixture
def sample_quantum():
    return [128, 64, 192, 32, 160, 96, 224, 16, 144, 80]


@pytest.fixture
def temp_data_dir():
    original_dir = None
    import src.data_handler as dh
    original_data_dir = dh.DATA_DIR
    original_classical = dh.CLASSICAL_FILE
    original_quantum = dh.QUANTUM_FILE
    with tempfile.TemporaryDirectory() as tmpdir:
        dh.DATA_DIR = tmpdir
        dh.CLASSICAL_FILE = os.path.join(tmpdir, "classical.csv")
        dh.QUANTUM_FILE = os.path.join(tmpdir, "quantum.csv")
        yield tmpdir
    dh.DATA_DIR = original_data_dir
    dh.CLASSICAL_FILE = original_classical
    dh.QUANTUM_FILE = original_quantum
