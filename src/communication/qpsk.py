import numpy as np


def generate_qpsk_signal(
    num_symbols=100,
    carrier_frequency=1000,
    sampling_rate=10000,
):

    # Generate random bits
    bits = np.random.randint(0, 2, 2 * num_symbols)

    # Group bits into pairs
    bit_pairs = bits.reshape(-1, 2)

    # QPSK mapping
    mapping = {

        (0, 0): 1 + 1j,
        (0, 1): -1 + 1j,
        (1, 0): 1 - 1j,
        (1, 1): -1 - 1j,

    }

    symbols = np.array(

        [mapping[tuple(pair)] for pair in bit_pairs]

    )

    samples_per_symbol = 100

    signal_symbols = np.repeat(
        symbols,
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

    qpsk_signal = np.real(

        signal_symbols * carrier

    )

    return time, qpsk_signal, bits