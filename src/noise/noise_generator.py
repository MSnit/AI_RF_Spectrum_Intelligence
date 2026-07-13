"""
noise_generator.py

Functions to add noise to RF signals.
"""

import numpy as np


def add_awgn(signal: np.ndarray, noise_std: float):
    """
    Add Additive White Gaussian Noise (AWGN) to a signal.

    Parameters
    ----------
    signal : np.ndarray
        Input signal.

    noise_std : float
        Standard deviation of the Gaussian noise.

    Returns
    -------
    noisy_signal : np.ndarray
        Signal with added noise.
    """

    noise = np.random.normal(
        loc=0,
        scale=noise_std,
        size=signal.shape
    )

    noisy_signal = signal + noise

    return noisy_signal

