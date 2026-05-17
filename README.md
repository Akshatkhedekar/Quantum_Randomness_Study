#  True Randomness Experiment: Quantum vs. Classical RNG

[![Python 3.8+](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Qiskit](https://img.shields.io/badge/Qiskit-1.0+-purple.svg)](https://qiskit.org/)
[![Research](https://img.shields.io/badge/Research-Quantum_Cryptography-red.svg)]()

> **"Classical randomness is an illusion. Quantum randomness is reality."**

##  Table of Contents

- [Overview](#overview)
- [The Problem](#the-problem)
- [Key Insight](#key-insight)
- [Project Structure](#project-structure)
- [Theory](#theory)
  - [Classical PRNG](#classical-prng)
  - [Quantum QRNG](#quantum-qrng)
  - [Comparison Table](#comparison-table)
- [Installation](#installation)
- [Why Quantum is "Physically Random"](#why-quantum-is-physically-random)
- [Cybersecurity Implications](#cybersecurity-implications)
- [Conclusion](#conclusion)
- [References](#references)

---



##  Overview

This research project demonstrates the fundamental difference between **deterministic pseudorandom numbers** (classical computers) and **truly random numbers** (quantum computers). We generate and compare random numbers using:

- **Step 1:** Python's `random` module (Mersenne Twister PRNG)
- **Step 2:** IBM's Qiskit (quantum superposition measurement)
- **Step 3:** Statistical visualization and predictability analysis

---

##  The Problem

### Classical computers CANNOT generate true randomness

Classical computers are **deterministic machines** — they follow strict rules. Every "random" number they generate comes from an algorithm with a hidden pattern.
"Anyone who considers arithmetical methods of producing random digits is,
of course, in a state of sin." — John von Neumann


### Modern AI can hack pseudorandom generators

With enough samples, machine learning can:
- Reverse-engineer the internal state of PRNGs
- Predict all future "random" numbers
- Break cryptographic keys that depend on them

---

##  Key Insight

| Aspect | Classical PRNG | Quantum QRNG |
|--------|---------------|--------------|
| Nature | Deterministic | Indeterministic |
| Source | Mathematical algorithm | Quantum measurement |
| Predictable? |  Yes (with enough data) |  No (fundamentally impossible) |
| AI can hack? |  Yes |  No |
| Security | Low | Unbreakable |

---

## Project Structure

```text
true-randomness-experiment/
│
├── README.md                        # Project documentation
├── requirements.txt                 # Python dependencies
│
├── src/
│   ├── classical_rng.py             # Python PRNG numbers
│   ├── quantum_rng.py               # Qiskit QRNG numbers
│   └── compare.py                   # Comparing Predictablility  
│
├── results/
│   ├── classical_histogram.png      # Classical random histogram
│   ├── quantum_histogram.png        # Quantum random histogram
│   └── comparison.png               # Histogram comparison plot
│
└── docs/
    └── theory.md                    # Extended documentation
```

##  Theory

### Classical PRNG (Pseudorandom Number Generation)

Python's `random` module uses the **Mersenne Twister** algorithm — a deterministic mathematical formula.

**Simplified example (Linear Congruential Generator):**
|ψ⟩ = α|0⟩ + β|1⟩


**Properties:**
-  **Periodic** — Eventually repeats
-  **Predictable** — Given state, all future numbers known
-  **No entropy** — Just mathematical scrambling
-  **Looks random** — Passes statistical tests

**Security flaw:** If an adversary sees ~624 consecutive outputs, they can reconstruct the entire internal state and predict everything that follows.

---

### Quantum QRNG (Quantum Random Number Generation)

Quantum mechanics is **fundamentally unpredictable**. A qubit in superposition has no definite value until measured.

**The quantum state:**
|ψ⟩ = α|0⟩ + β|1⟩


Where |α|² + |β|² = 1

**Measurement outcomes:**
- `0` with probability |α|²
- `1` with probability |β|²

**With a Hadamard gate (α = β = 1/√2):**
P(0) = 0.5
P(1) = 0.5

**Properties:**
-  **Genuinely random** — No hidden variables (Bell's theorem)
-  **Collapses on measurement** — State is destroyed
-  **Non-periodic** — Never repeats
-  **Unpredictable** — Even with perfect knowledge

**Security advantage:** No algorithm — including future AI — can predict the next bit better than a 50% guess.

---

### Comparison Table

| Feature | Classical (Python `random`) | Quantum (Qiskit) |
|---------|----------------------------|------------------|
| **Method** | Mersenne Twister | Hadamard gate + measurement |
| **Randomness type** | Algorithmic (pseudo) | Intrinsic (true) |
| **Source of entropy** | Seed (deterministic) | Quantum superposition collapse |
| **Reproducible with same seed** |  Yes |  No |
| **Periodic** |  Yes (2^19937-1) |  No |
| **Predictable by AI** |  Yes (with enough samples) |  No (theoretically impossible) |
| **Speed** |  Very fast (~10M/sec) |  Slow (~1k/sec simulated) |
| **Security level** |  Low (broken by AI) |  Unbreakable |
| **Use case** | Games, simulations | Cryptography, QKD |

---

##  Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager
- Internet connection (for Qiskit installation)

### Step-by-step setup

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/true-randomness-experiment.git
cd true-randomness-experiment

# 2. Create a virtual environment (recommended)
python -m venv venv

# 3. Activate the environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Verify Qiskit installation
python -c "from qiskit import QuantumCircuit; print('Qiskit ready!')"
 ```
## Why Quantum is "Physically Random"

Classical PRNGs are mathematically random but deterministic and reproducible. Quantum QRNGs are based on superposition measurement, which is fundamentally unpredictable. Even with perfect knowledge of the quantum circuit, no AI can predict the next bit better than a 50% guess. Hence, quantum randomness comes from nature's inherent indeterminism, not from a hidden algorithm.

## Cybersecurity Implications

- Pseudorandom generators can be hacked by AI because they follow learnable patterns.
- Quantum random number generators are unhackable in principle.
- QRNGs are essential for unbreakable cryptographic keys and Quantum Key Distribution (QKD).
- Classical RNGs are vulnerable for passwords, encryption, and blockchain security.

## Conclusion
**Classical randomness is an illusion. Quantum randomness is reality.**

Classical PRNG: Fast but insecure against AI attacks.

Quantum QRNG: Slow but provably secure.

Both methods can produce uniform distributions. The difference is not in how they look, it's in whether a pattern exists to be discovered.
For future unbreakable cybersecurity, migrate from pseudorandom number generators (PRNGs) to quantum random number generators (QRNGs) in security-critical applications.

## References

1. Nielsen, M. A., & Chuang, I. L. (2010). *Quantum Computation and Quantum Information*. Cambridge University Press.
2. Matsumoto, M., & Nishimura, T. (1998). Mersenne twister. *ACM Transactions on Modeling and Computer Simulation*.
3. IBM Qiskit Documentation: https://qiskit.org
4. NIST Random Bit Generation: https://csrc.nist.gov/projects/random-bit-generation
