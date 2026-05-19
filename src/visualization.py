"""
Visualization module for random number analysis.
Provides plots to support statistical findings visually.
"""

import os
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


def plot_histogram(classical, quantum, bins=50, save_path=None):
    """
    Side-by-side histograms comparing classical vs quantum distributions.

    Args:
        classical: List of classical random numbers
        quantum: List of quantum random numbers
        bins: Number of bins for histogram (default: 50)
        save_path: Optional file path to save the plot
    """
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))

    ax1.hist(classical, bins=bins, range=(0, 256), color="steelblue", edgecolor="black", alpha=0.7)
    ax1.set_title("Classical Distribution")
    ax1.set_xlabel("Value (0\u2013255)")
    ax1.set_ylabel("Frequency")
    ax1.grid(True, alpha=0.3, linestyle="--")

    ax2.hist(quantum, bins=bins, range=(0, 256), color="forestgreen", edgecolor="black", alpha=0.7)
    ax2.set_title("Quantum Distribution")
    ax2.set_xlabel("Value (0\u2013255)")
    ax2.set_ylabel("Frequency")
    ax2.grid(True, alpha=0.3, linestyle="--")

    plt.tight_layout()
    if save_path:
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        plt.savefig(save_path, dpi=300, bbox_inches="tight")
    plt.show()


def plot_kde(classical, quantum, save_path=None):
    """
    KDE plot overlaying both distributions on the same axes.

    Args:
        classical: List of classical random numbers
        quantum: List of quantum random numbers
        save_path: Optional file path to save the plot
    """
    sns.kdeplot(classical, label="Classical", color="steelblue", fill=True, alpha=0.3)
    sns.kdeplot(quantum, label="Quantum", color="forestgreen", fill=True, alpha=0.3)
    plt.title("Distribution Comparison (KDE)")
    plt.xlabel("Value (0\u2013255)")
    plt.ylabel("Density")
    plt.legend()
    plt.grid(True, alpha=0.3, linestyle="--")
    if save_path:
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        plt.savefig(save_path, dpi=300, bbox_inches="tight")
    plt.show()


def plot_lag(data, title, save_path=None):
    """
    Lag plot: x(n) vs x(n+1) to check for sequential patterns.

    Random data should show no structure (cloud of points).

    Args:
        data: List of numbers
        title: Label for the plot title
        save_path: Optional file path to save the plot
    """
    plt.figure(figsize=(6, 5))
    plt.scatter(data[:-1], data[1:], s=1, alpha=0.5, color="steelblue")
    plt.title(f"Lag Plot - {title}")
    plt.xlabel("x(n)")
    plt.ylabel("x(n+1)")
    plt.grid(True, alpha=0.3, linestyle="--")
    if save_path:
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        plt.savefig(save_path, dpi=300, bbox_inches="tight")
    plt.show()
