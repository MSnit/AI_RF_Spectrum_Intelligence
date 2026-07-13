"""
spectrogram.py

Functions for generating spectrograms.
"""

import matplotlib.pyplot as plt


def plot_spectrogram(signal, sampling_rate):
    """
    Plot spectrogram of a signal.
    """

    plt.figure(figsize=(10, 5))

    plt.specgram(
        signal,
        Fs=sampling_rate,
        NFFT=128,
        noverlap=64,
        cmap="viridis",
    )

    plt.title("Signal Spectrogram")
    plt.xlabel("Time (seconds)")
    plt.ylabel("Frequency (Hz)")
    plt.colorbar(label="Power (dB)")

    plt.tight_layout()
    plt.show()