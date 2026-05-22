from src.classical_rng import generate_random_numbers


def test_generates_correct_count():
    result = generate_random_numbers(100)
    assert len(result) == 100


def test_values_in_range():
    result = generate_random_numbers(1000)
    assert all(0 <= v <= 255 for v in result)


def test_deterministic_seed():
    a = generate_random_numbers(50, seed=42)
    b = generate_random_numbers(50, seed=42)
    assert a == b


def test_different_seeds_different():
    a = generate_random_numbers(50, seed=1)
    b = generate_random_numbers(50, seed=2)
    assert a != b
