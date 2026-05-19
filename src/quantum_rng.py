"""
Quantum Random Number Generator
Using IBM Qiskit - Qubit Superposition and Measurement

How it works:
1. Create a qubit in |0⟩ state
2. Apply Hadamard gate (H) - puts qubit in superposition
3. Measure - collapses randomly to 0 or 1
4. Repeat for each bit
"""

from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator


def get_quantum_bits(total_bits):
    """
    Generate random bits using quantum superposition.

    Physics behind it:
    |0⟩ ---[H]--- (|0⟩ + |1⟩)/√2 ---[Measure]--- 0 or 1 (random!)

    Args:
        total_bits: Number of random bits to generate

    Returns:
        List of 0s and 1s
    """
    circuit = QuantumCircuit(1, 1)
    circuit.h(0)
    circuit.measure(0, 0)

    simulator = AerSimulator()
    compiled_circuit = transpile(circuit, simulator)
    job = simulator.run(compiled_circuit, shots=total_bits, memory=True)
    result = job.result()

    raw_bits = result.get_memory()
    bits = [int(b) for b in raw_bits]

    return bits


def convert_bits_to_bytes(bits):
    """
    Convert bits (0/1 list) to bytes (0-255 numbers).
    8 bits make 1 byte = 1 number.

    Args:
        bits: List of 0s and 1s

    Returns:
        List of integers in range [0, 255]
    """
    numbers = []
    for i in range(0, len(bits) - 7, 8):
        eight_bits = bits[i:i+8]
        bit_string = "".join(str(b) for b in eight_bits)
        num = int(bit_string, 2)
        numbers.append(num)
    return numbers


def generate_quantum_numbers(how_many=10000):
    """
    Generate quantum random numbers.

    Args:
        how_many: Number of random numbers needed (range 0-255)

    Returns:
        List of random integers in range [0, 255]
    """
    total_bits_needed = how_many * 8
    bits = get_quantum_bits(total_bits_needed)
    numbers = convert_bits_to_bytes(bits)
    return numbers[:how_many]
