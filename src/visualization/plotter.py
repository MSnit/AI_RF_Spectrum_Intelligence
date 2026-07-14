"""
plotter.py

Visualization functions for RF signals.
"""

import matplotlib.pyplot as plt
import numpy as np


def plot_time_signal(
    time: np.ndarray,
    signal: np.ndarray,
    title: str = "Time Domain Signal",
):
    """
    Plot a signal in the time domain.
    """

    plt.figure(figsize=(10, 4))

    plt.plot(time, signal)

    plt.title(title)
    plt.xlabel("Time (seconds)")
    plt.ylabel("Amplitude")

    plt.grid(True)

    plt.tight_layout()

    return plt.gcf()


def plot_frequency_spectrum(
    frequencies: np.ndarray,
    magnitude: np.ndarray,
    title: str = "Frequency Spectrum",
):
    """
    Plot the frequency spectrum.
    """

    plt.figure(figsize=(10, 4))

    plt.plot(frequencies, magnitude)

    plt.title(title)
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Magnitude")

    plt.grid(True)

    plt.tight_layout()

    return plt.gcf()