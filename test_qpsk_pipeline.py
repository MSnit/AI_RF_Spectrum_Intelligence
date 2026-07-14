from src.communication.qpsk import generate_qpsk_signal

from src.signal_processing.fft_processor import compute_fft

from src.visualization.plotter import (
    plot_time_signal,
    plot_frequency_spectrum,
)

from src.feature_extraction.spectrogram import (
    plot_spectrogram,
)


time, signal, bits = generate_qpsk_signal()


plot_time_signal(

    time,
    signal,
    title="QPSK Time Domain",

)


frequencies, magnitude = compute_fft(

    signal,
    10000,

)


plot_frequency_spectrum(

    frequencies,
    magnitude,
    title="QPSK Frequency Spectrum",

)


plot_spectrogram(

    signal,
    10000,

)


print(bits[:20])