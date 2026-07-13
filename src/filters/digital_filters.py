"""
digital_filters.py

Digital filtering functions.
"""

import numpy as np
from scipy.signal import butter, filtfilt


def low_pass_filter(
    signal: np.ndarray,
    cutoff_frequency: float,
    sampling_rate: int,
    order: int = 4,
):
    """
    Apply a Butterworth Low-Pass Filter.
    """

    nyquist = sampling_rate / 2

    normalized_cutoff = cutoff_frequency / nyquist

    b, a = butter(
        order,
        normalized_cutoff,
        btype="low"
    )

    filtered_signal = filtfilt(
        b,
        a,
        signal
    )

    return filtered_signal