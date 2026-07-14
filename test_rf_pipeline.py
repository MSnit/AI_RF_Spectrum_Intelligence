from src.pipeline.rf_pipeline import run_pipeline
from src.visualization.plotter import (
    plot_time_signal,
    plot_frequency_spectrum,
)
from src.feature_extraction.spectrogram import (
    plot_spectrogram,
)


results = run_pipeline(

    signal_type="BPSK",
    noise_std=0.3,
    cutoff_frequency=2500,

)


# Time domain

plot_time_signal(

    results["time"],
    results["filtered_signal"],
    title="BPSK Time Domain",

)


# FFT

plot_frequency_spectrum(

    results["fft_frequencies"],
    results["magnitude"],
    title="BPSK Frequency Spectrum",

)


# Spectrogram

plot_spectrogram(

    results["filtered_signal"],
    sampling_rate=10000,

)