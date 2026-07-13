from src.noise.noise_generator import add_awgn
from src.filters.digital_filters import low_pass_filter
from src.signal_generation.signal_generator import generate_multi_tone_signal
from src.signal_processing.fft_processor import compute_fft
from src.feature_extraction.spectrogram import plot_spectrogram
from src.visualization.plotter import (

    plot_time_signal,
    plot_frequency_spectrum,
)

from config import (
    SAMPLING_RATE,
    DURATION,
    FREQUENCIES,
    AMPLITUDES,
    NOISE_STD,
    LOWPASS_CUTOFF,
)

# Generate multi-tone signal
time, signal = generate_multi_tone_signal(
    frequencies=FREQUENCIES,
    amplitudes=AMPLITUDES,
    sampling_rate=SAMPLING_RATE,
    duration=DURATION,
)

# Add AWGN noise
noisy_signal = add_awgn(
    signal,
    noise_std=NOISE_STD,
)

# Apply Low-Pass Filter
filtered_signal = low_pass_filter(
    noisy_signal,
    cutoff_frequency=LOWPASS_CUTOFF,
    sampling_rate=SAMPLING_RATE,
)

# Plot filtered signal
plot_time_signal(
    time,
    filtered_signal,
    title="Filtered Time Domain Signal",
)

# Compute FFT
frequencies, magnitude = compute_fft(
    filtered_signal,
    SAMPLING_RATE,
)

# Plot frequency spectrum
plot_frequency_spectrum(
    frequencies,
    magnitude,
    title="Filtered Frequency Spectrum",
)

plot_spectrogram(
    filtered_signal,
    SAMPLING_RATE,
)