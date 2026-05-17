# "True" Randomness Experiment: Quantum vs. Classical Random Number Generation

## Objective

To demonstrate the fundamental difference between **deterministic pseudorandom numbers** (classical) and **inherently probabilistic quantum random numbers**, and to explain why only the latter can be considered "truly random" in a physical sense.

## Background Theory

### Classical Pseudorandom Number Generation (PRNG)

Classical computers are deterministic finite-state machines. A PRNG (e.g., Python's `random` module, which uses the Mersenne Twister algorithm) starts from a **seed** (often the system time) and applies a deterministic recurrence.

**Example (simplified Linear Congruential Generator):**

|ψ⟩ = α|0⟩ + β|1⟩

**Key properties:**
- **Periodic:** After enough iterations, the sequence repeats.
- **Predictable:** Given current state, all future numbers are determined.
- **No true entropy source** – only algorithmic scrambling.

> **Consequence for cybersecurity:** If an adversary knows the algorithm and enough consecutive outputs, they can reconstruct the internal state and predict all future "random" numbers. Modern AI can accelerate this prediction via pattern recognition.

### Quantum Random Number Generation (QRNG)

Quantum mechanics is intrinsically non-deterministic. Measurement outcomes of a system in **superposition** cannot be predicted except in terms of probabilities.

**The core quantum principle:**

A qubit in superposition is in the state:


where |α|² + |β|² = 1.

When measured in the computational basis:
- Outcome `0` with probability |α|²
- Outcome `1` with probability |β|²

If α = β = 1/√2 (applying a Hadamard gate to |0⟩):
P(0) = 0.5, P(1) = 0.5

**Key quantum properties:**
- **No hidden variables** (per Bell's theorem & experimental violations of local realism) – the outcome is fundamentally random, not merely unknown.
- **Non-repeatable measurement** – measuring collapses the state; the same qubit cannot give the same sequence if reset and re-measured.
- **No periodicity** – truly random, infinite entropy per bit (under ideal conditions).

> **Consequence for cybersecurity:** Even with full knowledge of the quantum circuit, no algorithm (including AI) can predict the next bit better than a 50% guess. This forms the basis for **Quantum Key Distribution (QKD)**.

## Experimental Design Summary

| Feature | Classical (Python `random`) | Quantum (Qiskit simulator) |
|---------|-----------------------------|-----------------------------|
| Method | Mersenne Twister | Hadamard gate on \|0⟩, then measure |
| Randomness type | Algorithmic (pseudo) | Intrinsic (true) |
| Source of entropy | Seed (deterministic) | Quantum superposition collapse |
| Reproducible with same seed | Yes | No (even with identical circuit) |
| Predictable by AI | Yes (with enough samples) | No (fundamentally limited) |

## Why Quantum Is "Physically Random" (Explanation for Leads)

> **Pseudorandom (Python):**  
> The sequence is **mathematically random** in the sense of passing statistical tests, but it is **reproducible** and **deterministic**. Given the same seed or a few consecutive values, a powerful AI can reverse-engineer the internal state. This is a mathematical illusion of randomness.

> **Quantum (Qiskit):**  
> The randomness comes from **measurement of a superposition state**. According to quantum theory, nature does not pre-assign the outcome. Even if you built the exact same circuit billions of times, the sequence of bits would differ each time in an unpredictable way. This is **physical randomness** – a law-of-nature limitation on predictability, not a computational weakness.

> **Key distinction for cybersecurity:**  
> A pseudorandom generator can be "hacked" by AI because it follows a hidden but learnable pattern. A quantum random number generator is unhackable in principle – the only way to know the next bit is to measure it, and measurement changes the system (no cloning theorem).

## Expected Results & Plot Interpretation

In the distribution plots:

- **Classical PRNG:** Uniform distribution (if seeded well) – looks random, but mathematically structured.
- **Quantum QRNG:** Also uniform – but the underlying source is **irreducible entropy**.

> **Important note:** Visual uniformity alone is not the differentiator. Both methods can produce flat histograms. The difference is in **predictability**, not appearance.
Do not judge by histogram alone. Run a predictability test (e.g., train an AI on the first 80% of bits to predict the remaining 20%). Quantum bits will show near-50% prediction accuracy; classical bits (with a long enough sequence) may show higher accuracy.

## Conclusion

- **Python's `random`** = fast, cheap, but insecure against advanced AI/pattern analysis.
- **Qiskit's quantum random** = slower (currently), but **provably secure** based on quantum mechanical axioms.
- For future unbreakable encryption, migrate from PRNGs to QRNGs in security-critical applications.

---

## References

1. Nielsen, M. A., & Chuang, I. L. (2010). *Quantum Computation and Quantum Information: 10th Anniversary Edition*. Cambridge University Press.
2. Matsumoto, M., & Nishimura, T. (1998). Mersenne twister: a 623-dimensionally equidistributed uniform pseudorandom number generator. *ACM Transactions on Modeling and Computer Simulation*.
3. IBM Qiskit Documentation: https://qiskit.org/
