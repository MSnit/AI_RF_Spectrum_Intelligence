from src.communication.bpsk import generate_bpsk_signal
from src.signal_processing.fft_processor import compute_fft
from src.feature_extraction.spectrogram import plot_spectrogram
from src.visualization.plotter import (
    plot_time_signal,
    plot_frequency_spectrum,
)

# Generate BPSK signal
time, signal, bits = generate_bpsk_signal()

# Plot the time-domain signal
plot_time_signal(
    time,
    signal,
    title="BPSK Time Domain Signal",
)

# Compute FFT
frequencies, magnitude = compute_fft(
    signal,
    sampling_rate=10000,
)

# Plot the frequency spectrum
plot_frequency_spectrum(
    frequencies,
    magnitude,
    title="BPSK Frequency Spectrum",
)

# Print the first 20 generated bits
print("\nFirst 20 Bits:")
print(bits[:20])

# Generate Spectrogram
plot_spectrogram(
    signal,
    sampling_rate=10000,
)