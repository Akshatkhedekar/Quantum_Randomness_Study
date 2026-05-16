"""
Classical Random Number Generator

"""

import random
import matplotlib.pyplot as plt
import numpy as np

def generate_random_numbers(total_numbers=10000):
    """
    Generate classical random numbers
    Range: 0 to 255 (like a byte)

    """
    numbers = []
    for i in range(total_numbers):
        num = random.randint(0, 255)
        numbers.append(num)
    return numbers

def show_statistics(numbers):
    """Print basic statistics"""
    print("=" * 40)
    print("CLASSICAL RANDOM NUMBERS - STATISTICS")
    print("=" * 40)
    print(f"Total numbers generated: {len(numbers)}")
    print(f"Minimum value: {min(numbers)}")
    print(f"Maximum value: {max(numbers)}")
    print(f"Average (mean): {sum(numbers)/len(numbers):.2f}")
    print(f"Standard deviation: {np.std(numbers):.2f}")
    print("\nFirst 20 numbers:")
    print(numbers[:20])

def plot_histogram(numbers):
    """Plot the distribution"""
    plt.figure(figsize=(10, 6))
    plt.hist(numbers, bins=50, color='skyblue', edgecolor='black', alpha=0.7)
    plt.title("Classical Pseudorandom Number Distribution", fontsize=14, fontweight='bold')
    plt.xlabel("Value (0-255)", fontsize=12)
    plt.ylabel("Frequency", fontsize=12)
    plt.grid(True, alpha=0.3, linestyle='--')
    plt.show()

def save_to_file(numbers, filename="classical_numbers.txt"):
    """Save numbers to a text file"""
    with open(filename, 'w') as f:
        for num in numbers:
            f.write(str(num) + '\n')
    print(f"\nNumbers saved to {filename}")


#Main code part

if __name__ == "__main__":
    print("🔢 Generating Classical Random Numbers...")
    print("-" * 40)
    
    # Generating numbers
    my_numbers = generate_random_numbers(10000)
    
    # Stats
    show_statistics(my_numbers)
    
    # Plotting graph
    plot_histogram(my_numbers)
    
    # Save to file 
    save_to_file(my_numbers)
    
    print("\n This is the histogram for classical random numbers.")