from src.quantum_rng import convert_bits_to_bytes, generate_quantum_numbers


def test_convert_bits_to_bytes_length():
    bits = [0, 0, 0, 0, 0, 0, 0, 0]
    assert len(convert_bits_to_bytes(bits)) == 1

    bits = [0] * 16
    assert len(convert_bits_to_bytes(bits)) == 2

    bits = [0] * 7
    assert len(convert_bits_to_bytes(bits)) == 0


def test_convert_bits_to_bytes_correctness():
    bits = [1, 0, 1, 0, 1, 0, 1, 0]
    result = convert_bits_to_bytes(bits)
    assert result == [170]

    bits = [1, 1, 1, 1, 1, 1, 1, 1]
    result = convert_bits_to_bytes(bits)
    assert result == [255]

    bits = [0, 0, 0, 0, 0, 0, 0, 0]
    result = convert_bits_to_bytes(bits)
    assert result == [0]


def test_generate_quantum_numbers_count():
    result = generate_quantum_numbers(10)
    assert len(result) == 10


def test_quantum_numbers_in_range():
    result = generate_quantum_numbers(100)
    assert all(0 <= v <= 255 for v in result)
