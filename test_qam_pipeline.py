from src.communication.qam import generate_qam_signal

from src.signal_processing.fft_processor import compute_fft

from src.visualization.plotter import (
    plot_time_signal,
    plot_frequency_spectrum,
)

from src.feature_extraction.spectrogram import (
    plot_spectrogram,
)


time, signal, bits = generate_qam_signal()


plot_time_signal(
    time,
    signal,
    title="16-QAM Time Domain",
)


frequencies, magnitude = compute_fft(
    signal,
    10000,
)


plot_frequency_spectrum(
    frequencies,
    magnitude,
    title="16-QAM Frequency Spectrum",
)


plot_spectrogram(
    signal,
    10000,
)


print(bits[:20])