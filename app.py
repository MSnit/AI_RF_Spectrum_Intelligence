import streamlit as st

from src.pipeline.rf_pipeline import run_pipeline

from src.visualization.plotter import (
    plot_time_signal,
    plot_frequency_spectrum,
)

from src.feature_extraction.spectrogram import (
    plot_spectrogram,
)

# --------------------------------------------------

st.set_page_config(
    page_title="AI RF Spectrum Intelligence",
    page_icon="📡",
    layout="wide",
)

st.title("📡 AI-Powered RF Spectrum Intelligence Platform")

# --------------------------------------------------

st.sidebar.header("Signal Configuration")

signal_type = st.sidebar.selectbox(
    "Signal Type",
    [
        "MULTI_TONE",
        "BPSK",
    ],
)

# --------------------------------------------------

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

# --------------------------------------------------

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

# --------------------------------------------------

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

# --------------------------------------------------

run = st.sidebar.button("▶ Run Analysis")

# --------------------------------------------------

st.header("Current Parameters")

col1, col2 = st.columns(2)

with col1:
    st.write("### Signal Settings")
    st.write(f"Signal Type : {signal_type}")
    st.write(f"Frequency 1 : {freq1} Hz")
    st.write(f"Frequency 2 : {freq2} Hz")
    st.write(f"Frequency 3 : {freq3} Hz")

with col2:
    st.write("### Processing")
    st.write(f"Noise Std : {noise}")
    st.write(f"Cutoff : {cutoff} Hz")

# --------------------------------------------------

if run:

    results = run_pipeline(

        signal_type=signal_type,
        noise_std=noise,
        cutoff_frequency=cutoff,
        frequencies=[freq1, freq2, freq3],
        amplitudes=[amp1, amp2, amp3],

    )

    st.success("Analysis Complete ✅")

    # ----------------------------------------------

    st.subheader("Time Domain Signal")

    fig1 = plot_time_signal(

        results["time"],
        results["filtered_signal"],
        title="Filtered Time Domain Signal",

    )

    st.pyplot(fig1)

    # ----------------------------------------------

    st.subheader("Frequency Spectrum")

    fig2 = plot_frequency_spectrum(

        results["fft_frequencies"],
        results["magnitude"],
        title="Filtered Frequency Spectrum",

    )

    st.pyplot(fig2)

    # ----------------------------------------------

    st.subheader("Spectrogram")

    fig3 = plot_spectrogram(

        results["filtered_signal"],
        10000,

    )

    st.pyplot(fig3)

    "QPSK",