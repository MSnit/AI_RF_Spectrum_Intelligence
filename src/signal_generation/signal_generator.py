"""
signal_generator.py

This module contains functions to generate RF signals.
"""

import numpy as np


def generate_sine_wave(
    frequency: float,
    amplitude: float,
    sampling_rate: int,
    duration: float
):
    """
    Generate a sine wave.

    Parameters
    ----------
    frequency : float
        Frequency of the signal in Hz.

    amplitude : float
        Peak amplitude of the signal.

    sampling_rate : int
        Number of samples per second.

    duration : float
        Duration of the signal in seconds.

    Returns
    -------
    time : np.ndarray
        Time vector.

    signal : np.ndarray
        Generated sine wave.
    """

    # Create time vector
    time = np.linspace(
        0,
        duration,
        int(sampling_rate * duration),
        endpoint=False
    )

    # Generate sine wave
    signal = amplitude * np.sin(2 * np.pi * frequency * time)

    return time, signal

def generate_multi_tone_signal(
    frequencies: list[float],
    amplitudes: list[float],
    sampling_rate: int,
    duration: float,
):
    """
    Generate a signal containing multiple sine waves.
    """

    if len(frequencies) != len(amplitudes):
        raise ValueError("frequencies and amplitudes must have the same length.")

    time = np.linspace(
        0,
        duration,
        int(sampling_rate * duration),
        endpoint=False,
    )

    signal = np.zeros_like(time)

    for frequency, amplitude in zip(frequencies, amplitudes):
        signal += amplitude * np.sin(2 * np.pi * frequency * time)

    return time, signal