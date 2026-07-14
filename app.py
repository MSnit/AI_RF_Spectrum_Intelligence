import streamlit as st
from src.signal_generation.signal_generator import generate_multi_tone_signal
from src.noise.noise_generator import add_awgn
from src.filters.digital_filters import low_pass_filter
from src.signal_processing.fft_processor import compute_fft
from src.visualization.plotter import (
    plot_time_signal,
    plot_frequency_spectrum,
)
from src.feature_extraction.spectrogram import plot_spectrogram

st.set_page_config(
    page_title="AI RF Spectrum Intelligence",
    page_icon="📡",
    layout="wide",
)

st.title("📡 AI-Powered RF Spectrum Intelligence Platform")

st.sidebar.header("Signal Configuration")

freq1 = st.sidebar.number_input(
    "Frequency 1 (Hz)",
    min_value=100,
    max_value=5000,
    value=1000,
)

freq2 = st.sidebar.number_input(
    "Frequency 2 (Hz)",
    min_value=100,
    max_value=5000,
    value=2000,
)

freq3 = st.sidebar.number_input(
    "Frequency 3 (Hz)",
    min_value=100,
    max_value=5000,
    value=3500,
)

amp1 = st.sidebar.slider(
    "Amplitude 1",
    0.0,
    2.0,
    1.0,
)

amp2 = st.sidebar.slider(
    "Amplitude 2",
    0.0,
    2.0,
    0.5,
)

amp3 = st.sidebar.slider(
    "Amplitude 3",
    0.0,
    2.0,
    0.8,
)

noise = st.sidebar.slider(
    "Noise Standard Deviation",
    0.0,
    1.0,
    0.3,
)

cutoff = st.sidebar.slider(
    "Low-Pass Cutoff (Hz)",
    500,
    5000,
    2500,
)

run = st.sidebar.button("▶ Run Analysis")

st.header("Current Parameters")

col1, col2 = st.columns(2)

with col1:
    st.write("### Signal Frequencies")
    st.write(f"Frequency 1 : {freq1} Hz")
    st.write(f"Frequency 2 : {freq2} Hz")
    st.write(f"Frequency 3 : {freq3} Hz")

with col2:
    st.write("### Processing")
    st.write(f"Noise Std : {noise}")
    st.write(f"Cutoff : {cutoff} Hz")

if run:

    SAMPLING_RATE = 10000
    DURATION = 0.01

    # Generate RF Signal
    time, signal = generate_multi_tone_signal(
        frequencies=[freq1, freq2, freq3],
        amplitudes=[amp1, amp2, amp3],
        sampling_rate=SAMPLING_RATE,
        duration=DURATION,
    )

    # Add Noise
    noisy_signal = add_awgn(
        signal,
        noise_std=noise,
    )

    # Filter Signal
    filtered_signal = low_pass_filter(
        noisy_signal,
        cutoff_frequency=cutoff,
        sampling_rate=SAMPLING_RATE,
    )

    # FFT
    frequencies, magnitude = compute_fft(
        filtered_signal,
        SAMPLING_RATE,
    )

    st.success("Analysis Complete ✅")

    st.subheader("Time Domain Signal")

fig1 = plot_time_signal(
    time,
    filtered_signal,
    title="Filtered Time Domain Signal",
)

st.pyplot(fig1)

st.subheader("Frequency Spectrum")

fig2 = plot_frequency_spectrum(
    frequencies,
    magnitude,
    title="Filtered Frequency Spectrum",
)

st.pyplot(fig2)

st.subheader("Spectrogram")

fig3 = plot_spectrogram(
    filtered_signal,
    SAMPLING_RATE,
)

st.pyplot(fig3)