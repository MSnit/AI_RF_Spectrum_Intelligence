from src.communication.ofdm import generate_ofdm_signal
from src.signal_processing.fft_processor import compute_fft

from src.visualization.plotter import (
    plot_time_signal,
    plot_frequency_spectrum,
)

from src.feature_extraction.spectrogram import (
    plot_spectrogram,
)


time, signal = generate_ofdm_signal()

plot_time_signal(
    time,
    signal,
    title="OFDM Time Domain",
)

frequencies, magnitude = compute_fft(
    signal,
    10000,
)

plot_frequency_spectrum(
    frequencies,
    magnitude,
    title="OFDM Frequency Spectrum",
)

plot_spectrogram(
    signal,
    10000,
)