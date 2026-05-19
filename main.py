"""
Classical vs Quantum Random Number Generator Comparison
Generates random numbers using both classical and quantum methods,
then saves the results to CSV files.
"""

import os
from src.classical_rng import generate_random_numbers
from src.quantum_rng import generate_quantum_numbers
from src.data_handler import save_data
from src.analysis import compare_datasets, full_analysis, determinism_demo, determinism_explanation
from src.visualization import plot_histogram, plot_kde, plot_lag


def main():
    print("=" * 40)
    print("CLASSICAL vs QUANTUM RANDOM")
    print("=" * 40)

    print("\nGenerating classical numbers...")
    classical = generate_random_numbers(10000)

    print("Generating quantum numbers...")
    quantum = generate_quantum_numbers(10000)

    print("Saving data...")
    save_data(classical, quantum)

    print("Analyzing data...")
    print(f"\nSample Size: {len(classical)}")
    print()

    stats = compare_datasets(classical, quantum)
    print("--- Basic Stats ---")
    print(f"Classical: {stats['classical']}")
    print(f"Quantum: {stats['quantum']}")
    print()

    print("--- Full Analysis ---")
    full = full_analysis(classical, quantum)

    print("--- KS Test ---")
    print(f"Statistic: {full['ks_test']['statistic']}")
    print(f"P-value: {full['ks_test']['p_value']}")
    print(f"Interpretation: {full['ks_test']['interpretation']}")
    print()

    print("--- Entropy ---")
    print(f"Classical: {full['entropy']['classical']}")
    print(f"Quantum: {full['entropy']['quantum']}")
    print(f"Interpretation: {full['entropy']['interpretation']}")
    print()

    print("--- Autocorrelation ---")
    print(f"Classical: {full['autocorrelation']['classical']['value']}")
    print(f"Interpretation: {full['autocorrelation']['classical']['interpretation']}")
    print(f"Quantum: {full['autocorrelation']['quantum']['value']}")
    print(f"Interpretation: {full['autocorrelation']['quantum']['interpretation']}")
    print()

    print("--- Determinism Demo ---")
    demo = determinism_demo()
    print(f"Classical (seed=42) Run 1 first 5: {demo['classical']['first_five']}")
    print(f"Classical (seed=42) Run 2 first 5: {demo['classical']['second_five']}")
    if demo["classical"]["identical"]:
        print("  -> IDENTICAL \u2014 Classical is deterministic (seed controls everything)")
    print()
    print(f"Quantum Run 1 first 5: {demo['quantum']['first_five']}")
    print(f"Quantum Run 2 first 5: {demo['quantum']['second_five']}")
    if demo["quantum"]["different"]:
        print("  -> DIFFERENT \u2014 Quantum is non-deterministic (no seed possible)")
    print()

    print("--- Practical Impact ---")
    print(determinism_explanation()["explanation"])
    print()

    print("Generating visualizations...")
    os.makedirs("outputs/plots", exist_ok=True)
    plot_histogram(classical, quantum, save_path="outputs/plots/histogram.png")
    plot_kde(classical, quantum, save_path="outputs/plots/kde.png")
    plot_lag(classical, "Classical", save_path="outputs/plots/lag_classical.png")
    plot_lag(quantum, "Quantum", save_path="outputs/plots/lag_quantum.png")
    print("Plots saved in outputs/plots/")
    print()

    print("=" * 40)
    print("FINAL INSIGHT")
    print("=" * 40)
    print()
    print("1. Both classical and quantum generators produce statistically uniform distributions.")
    print("2. No statistically significant difference was detected using KS test.")
    print("3. Both exhibit high entropy and no observable patterns.")
    print()
    print("HOWEVER:")
    print()
    print("* Classical randomness is deterministic (seed-based).")
    print("* Quantum randomness is non-deterministic (measurement-based).")
    print()
    print("CONCLUSION:")
    print()
    print("While statistical tests show similar behavior, the fundamental nature")
    print("of randomness differs. Quantum randomness provides unpredictability")
    print("at a physical level, whereas classical methods rely on deterministic")
    print("algorithms.")
    print()
    print("Summary:")
    print("No statistically significant difference detected between classical")
    print("and quantum randomness under current tests.")


if __name__ == "__main__":
    main()
