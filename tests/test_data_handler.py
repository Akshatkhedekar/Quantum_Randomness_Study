import os
from src.data_handler import save_data, load_data, DATA_DIR, CLASSICAL_FILE, QUANTUM_FILE


def test_save_and_load_roundtrip(temp_data_dir):
    classical = [1, 2, 3]
    quantum = [4, 5, 6]
    save_data(classical, quantum)
    loaded_c, loaded_q = load_data()
    assert loaded_c == classical
    assert loaded_q == quantum


def test_load_nonexistent_returns_empty():
    loaded_c, loaded_q = load_data()
    if not os.path.exists(CLASSICAL_FILE):
        assert loaded_c == []
    if not os.path.exists(QUANTUM_FILE):
        assert loaded_q == []


def test_overwrite(temp_data_dir):
    save_data([1, 2, 3], [4, 5, 6])
    save_data([7, 8, 9], [10, 11, 12])
    loaded_c, loaded_q = load_data()
    assert loaded_c == [7, 8, 9]
    assert loaded_q == [10, 11, 12]
