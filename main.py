from src.noise.noise_generator import add_awgn
from src.filters.digital_filters import low_pass_filter
from src.signal_generation.signal_generator import generate_multi_tone_signal
from src.signal_processing.fft_processor import compute_fft
from src.visualization.plotter import (
    plot_time_signal,
    plot_frequency_spectrum,
)

SAMPLING_RATE = 10000

# Generate multi-tone signal
time, signal = generate_multi_tone_signal(
    frequencies=[1000, 2000, 3500],
    amplitudes=[1, 0.5, 0.8],
    sampling_rate=SAMPLING_RATE,
    duration=0.01,
)

# Add AWGN noise
noisy_signal = add_awgn(
    signal,
    noise_std=0.3,
)

# Apply Low-Pass Filter
filtered_signal = low_pass_filter(
    noisy_signal,
    cutoff_frequency=2500,
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