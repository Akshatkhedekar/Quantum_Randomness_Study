import random
from qiskit import QuantumCircuit, transpile # Import transpile
from qiskit_aer import AerSimulator
import matplotlib.pyplot as plt

#Classical Part
def make_classical_numbers(n):
    numbers = []
    for i in range(n):
        numbers.append(random.randint(0, 255))
    return numbers

#Quantum Part
def make_quantum_bits(n):
    circuit = QuantumCircuit(1, 1)
    circuit.h(0)
    circuit.measure(0, 0)
    
    simulator = AerSimulator()
    # Use transpile and set memory=True to get individual shot results
    compiled_circuit = transpile(circuit, simulator)
    job = simulator.run(compiled_circuit, shots=n, memory=True)
    result = job.result()
    
    # Get individual measurement outcomes and convert them to integers
    raw_bits = result.get_memory()
    bits = [int(b) for b in raw_bits]

    return bits

def bits_to_numbers(bits):
    numbers = []
    for i in range(0, len(bits)-7, 8):
        # 8 bits
        b = bits[i:i+8]
        # String
        s = ""
        for x in b:
            s = s + str(x)
        # Number
        num = int(s, 2)
        numbers.append(num)
    return numbers

def make_quantum_numbers(n):
    bits = make_quantum_bits(n * 8)
    numbers = bits_to_numbers(bits)
    return numbers[:n]

#Main Code
print("=" * 40)
print("CLASSICAL vs QUANTUM RANDOM")
print("=" * 40)

# Generate numbers
print("\n1. Generating classical numbers...")
classical = make_classical_numbers(10000)

print("2. Generating quantum numbers...")
quantum = make_quantum_numbers(10000)

# Plotting side by side
print("3. Plotting graphs...")

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))

ax1.hist(classical, bins=50, color='skyblue')
ax1.set_title("Classical (Fake Random)")
ax1.set_xlabel("Number")
ax1.set_ylabel("Count")

ax2.hist(quantum, bins=50, color='pink')
ax2.set_title("Quantum (Real Random)")
ax2.set_xlabel("Number")
ax2.set_ylabel("Count")

plt.tight_layout()
plt.show()

# Printing explanation
print("EXPLANATION")

print("""
Classical (Skyblue Graph):
Source: Mathematical algorithm (Mersenne Twister)
• Deterministic: Same seed → Same numbers
• Predictable: If formula and seed are known
• Attack possible: AI can learn the pattern
• Real randomness? NO

Quantum (Pink Graph):
Source: Qubit in superposition |+⟩ = (|0⟩+|1⟩)/√2
• Non-deterministic: Measurement outcome is fundamentally random
• Unpredictable: Even in principle cannot be predicted
• No pattern: Nothing to learn - even for AI
• Real randomness? YES
Physics basis: Born Rule - P(0)=|α|², P(1)=|β|²
• Bell's Theorem: No hidden variables exist
• Heisenberg Uncertainty: Measurement disturbs the state

Both graphs look uniform but quantum one is REAL random and classical one is FAKE random.
""")