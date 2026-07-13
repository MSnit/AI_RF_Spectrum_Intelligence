"""
fft_processor.py

Functions for Fast Fourier Transform (FFT).
"""

import numpy as np


def compute_fft(signal: np.ndarray, sampling_rate: int):
    """
    Compute the FFT of a signal.
    """

    n = len(signal)

    fft_values = np.fft.fft(signal)

    magnitude = np.abs(fft_values) / n

    frequencies = np.fft.fftfreq(n, d=1 / sampling_rate)

    positive = frequencies >= 0

    return frequencies[positive], magnitude[positive]