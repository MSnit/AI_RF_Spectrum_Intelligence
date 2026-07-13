from src.signal_generation.signal_generator import generate_multi_tone_signal
from src.signal_processing.fft_processor import compute_fft
from src.visualization.plotter import (
    plot_time_signal,
    plot_frequency_spectrum,
)

SAMPLING_RATE = 10000

# Generate signal
time, signal = generate_multi_tone_signal(
    frequencies=[1000, 2000, 3500],
    amplitudes=[1, 0.5, 0.8],
    sampling_rate=SAMPLING_RATE,
    duration=0.01,
)


# Plot time-domain signal
plot_time_signal(time, signal)

# Compute FFT
frequencies, magnitude = compute_fft(signal, SAMPLING_RATE)

# Plot frequency spectrum
plot_frequency_spectrum(frequencies, magnitude)