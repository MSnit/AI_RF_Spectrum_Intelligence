"""
bpsk.py

Binary Phase Shift Keying signal generation.
"""

import numpy as np


def generate_bpsk_signal(
    num_bits=100,
    carrier_frequency=1000,
    sampling_rate=10000,
):
    """
    Generate a BPSK signal.

    Parameters
    ----------
    num_bits : int
        Number of bits.

    carrier_frequency : int
        Carrier frequency in Hz.

    sampling_rate : int
        Sampling frequency.

    Returns
    -------
    time : np.ndarray

    signal : np.ndarray

    bits : np.ndarray
    """

    # Generate random bits
    bits = np.random.randint(0, 2, num_bits)

    # Map bits to symbols
    symbols = 2 * bits - 1

    # Samples per bit
    samples_per_bit = 100

    # Repeat symbols
    signal_symbols = np.repeat(
        symbols,
        samples_per_bit,
    )

    # Time vector
    time = np.arange(
        len(signal_symbols)
    ) / sampling_rate

    # Carrier signal
    carrier = np.cos(
        2 * np.pi *
        carrier_frequency *
        time
    )

    # BPSK modulation
    bpsk_signal = (
        signal_symbols *
        carrier
    )

    return time, bpsk_signal, bits