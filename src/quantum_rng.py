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
import matplotlib.pyplot as plt
import numpy as np

def get_quantum_bits(total_bits):
    """
    Generate random bits using quantum superposition
    
    Physics behind it:
    |0⟩ ---[H]--- (|0⟩ + |1⟩)/√2 ---[Measure]--- 0 or 1 (random!)
    """
    # Creating quantum circuit with 1 qubit and 1 classical bit
    circuit = QuantumCircuit(1, 1)
    
    # Apply Hadamard gate - creates superposition
    circuit.h(0)
    
    # Measure - collapses the wavefunction
    circuit.measure(0, 0)
    
    # Run on quantum simulator
    simulator = AerSimulator()
    # Use transpile and set memory=True to get individual results
    compiled_circuit = transpile(circuit, simulator)
    job = simulator.run(compiled_circuit, shots=total_bits, memory=True)
    result = job.result()
    
    # Get individual measurement outcomes and convert them to integers
    raw_bits = result.get_memory()
    bits = [int(b) for b in raw_bits]
    
    return bits

def convert_bits_to_bytes(bits):
    """
    Convert bits (0/1 list) to bytes (0-255 numbers)
    8 bits make 1 byte = 1 number
    """
    numbers = []
    
    # Every 8 bit will make a number
    for i in range(0, len(bits) - 7, 8):
        # 8 bits lelo
        eight_bits = bits[i:i+8]
        
        # Converting it to string        
        bit_string = ""
        for b in eight_bits:
            bit_string = bit_string + str(b)
        
        # Binary to integer conversion
        num = int(bit_string, 2)
        numbers.append(num)
    
    return numbers

def generate_quantum_numbers(how_many=10000):
    """
    Generate quantum random numbers
    how_many: numbers needed (0 to 255 range mein)
    """

    total_bits_needed = how_many * 8
    
    print(f"   Generating {total_bits_needed} quantum bits...")
    bits = get_quantum_bits(total_bits_needed)
    
    print(f"   Converting bits to numbers...")
    numbers = convert_bits_to_bytes(bits)
    
    return numbers[:how_many]

def show_statistics(numbers):
    """
    Print statistics about the numbers
    """
    print("=" * 40)
    print("QUANTUM RANDOM NUMBERS - STATISTICS")
    print("=" * 40)
    print(f"Total numbers generated: {len(numbers)}")
    print(f"Minimum value: {min(numbers)}")
    print(f"Maximum value: {max(numbers)}")
    print(f"Average (mean): {sum(numbers)/len(numbers):.2f}")
    print(f"Standard deviation: {np.std(numbers):.2f}")
    
    # Checking uniformity
    unique_count = len(set(numbers))
    print(f"Unique values: {unique_count} out of {len(numbers)}")
    
    print("\nFirst 20 numbers:")
    print(numbers[:20])

def plot_histogram(numbers):
    """
    Plot distribution histogram
    """
    plt.figure(figsize=(10, 6))
    plt.hist(numbers, bins=50, color='forestgreen', edgecolor='black', alpha=0.7)
    plt.title("Quantum Random Number Distribution (True Random)", fontsize=14, fontweight='bold')
    plt.xlabel("Value (0-255)", fontsize=12)
    plt.ylabel("Frequency", fontsize=12)
    plt.grid(True, alpha=0.3, linestyle='--')
    plt.show()

def save_to_file(numbers, filename="quantum_numbers.txt"):
    """
    Save numbers to text file
    """
    with open(filename, 'w') as f:
        for num in numbers:
            f.write(str(num) + '\n')
    print(f"\nNumbers saved to {filename}")

def explain_quantum_randomness():
    """
    Print explanation of how quantum randomness works
    """
    print("\n" + "=" * 40)
    print("HOW QUANTUM RANDOMNESS WORKS")
    print("=" * 40)
    print("""
    Step 1: Start with qubit in state |0⟩
    
    Step 2: Apply Hadamard (H) gate
            |0⟩  ---H---→  (|0⟩ + |1⟩)/√2
            Now qubit is in SUPERPOSITION
            Means: Both 0 and 1 simultaneously!
    
    Step 3: Measure the qubit
            Wavefunction COLLAPSES randomly
            50% chance → |0⟩
            50% chance → |1⟩
    
    Step 4: Repeat for each bit
    
    WHY IS THIS TRULY RANDOM?
    - No mathematical formula
    - No seed value
    - Nature's fundamental unpredictability
    - Cannot be predicted even with infinite computing power
    """)

#Main code part
if __name__ == "__main__":
    print("⚛️ GENERATING QUANTUM RANDOM NUMBERS")
    print("-" * 40)
    print("Using: Qubit Superposition + Measurement")
    print("Simulator: Qiskit Aer (IBM Quantum)")
    print("-" * 40)
    
    # Explaining the physics behind it
    explain_quantum_randomness()
    
    # Generating numbers
    print("\n🔄 Generating quantum numbers...")
    my_numbers = generate_quantum_numbers(10000)
    
    # Statistics
    show_statistics(my_numbers)
    
    # Plotting graph
    plot_histogram(my_numbers)
    
    # Save to file
    save_to_file(my_numbers)
    
    print("\n This is the histogram for quantum random numbers.")
