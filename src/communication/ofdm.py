import numpy as np


def generate_ofdm_signal(
    num_subcarriers=64,
    carrier_frequency=1000,
    sampling_rate=10000,
):

    # Generate random QPSK symbols
    data = np.random.choice(
        [-1 - 1j, -1 + 1j, 1 - 1j, 1 + 1j],
        size=num_subcarriers,
    )

    # Perform IFFT
    ofdm_symbols = np.fft.ifft(data)

    samples_per_symbol = 100

    signal_symbols = np.repeat(
        ofdm_symbols,
        samples_per_symbol,
    )

    time = np.arange(
        len(signal_symbols)
    ) / sampling_rate

    carrier = np.exp(
        1j * 2 * np.pi *
        carrier_frequency *
        time
    )

    ofdm_signal = np.real(
        signal_symbols * carrier
    )

    return time, ofdm_signal