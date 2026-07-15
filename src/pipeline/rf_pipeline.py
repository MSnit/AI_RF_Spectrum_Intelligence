from src.signal_generation.signal_generator import (
    generate_multi_tone_signal,
)

from src.communication.bpsk import (
    generate_bpsk_signal,
)

from src.communication.qpsk import (
    generate_qpsk_signal,
)

from src.noise.noise_generator import add_awgn
from src.filters.digital_filters import low_pass_filter
from src.signal_processing.fft_processor import compute_fft
from src.communication.qam import generate_qam_signal


def run_pipeline(
    signal_type,
    noise_std,
    cutoff_frequency,
    sampling_rate=10000,
    duration=0.01,
    frequencies=None,
    amplitudes=None,
):

    # Signal generation

    if signal_type == "MULTI_TONE":

        time, signal = generate_multi_tone_signal(
            frequencies=frequencies,
            amplitudes=amplitudes,
            sampling_rate=sampling_rate,
            duration=duration,
        )

    elif signal_type == "BPSK":

        time, signal, _ = generate_bpsk_signal(
            carrier_frequency=1000,
            sampling_rate=sampling_rate,
        )

    elif signal_type == "QPSK":

        time, signal, _ = generate_qpsk_signal(
            carrier_frequency=1000,
            sampling_rate=sampling_rate,
    )
        
    elif signal_type == "QAM":

        time, signal, _ = generate_qam_signal(
            carrier_frequency=1000,
            sampling_rate=sampling_rate,
    )

    else:

        raise ValueError("Unsupported signal type.")

    # Add noise

    noisy_signal = add_awgn(
        signal,
        noise_std=noise_std,
    )

    # Filter

    filtered_signal = low_pass_filter(
        noisy_signal,
        cutoff_frequency=cutoff_frequency,
        sampling_rate=sampling_rate,
    )

    # FFT

    fft_frequencies, magnitude = compute_fft(
        filtered_signal,
        sampling_rate,
    )

    return {

        "time": time,
        "signal": signal,
        "filtered_signal": filtered_signal,
        "fft_frequencies": fft_frequencies,
        "magnitude": magnitude,

    }


    