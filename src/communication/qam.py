import numpy as np


def generate_qam_signal(
    num_symbols=100,
    carrier_frequency=1000,
    sampling_rate=10000,
):

    # Generate random bits
    bits = np.random.randint(0, 2, 4 * num_symbols)

    # Group into 4-bit symbols
    bit_groups = bits.reshape(-1, 4)

    # 16-QAM mapping
    mapping = {

        (0, 0, 0, 0): -3 - 3j,
        (0, 0, 0, 1): -3 - 1j,
        (0, 0, 1, 0): -3 + 1j,
        (0, 0, 1, 1): -3 + 3j,

        (0, 1, 0, 0): -1 - 3j,
        (0, 1, 0, 1): -1 - 1j,
        (0, 1, 1, 0): -1 + 1j,
        (0, 1, 1, 1): -1 + 3j,

        (1, 0, 0, 0): 1 - 3j,
        (1, 0, 0, 1): 1 - 1j,
        (1, 0, 1, 0): 1 + 1j,
        (1, 0, 1, 1): 1 + 3j,

        (1, 1, 0, 0): 3 - 3j,
        (1, 1, 0, 1): 3 - 1j,
        (1, 1, 1, 0): 3 + 1j,
        (1, 1, 1, 1): 3 + 3j,

    }

    symbols = np.array(
        [mapping[tuple(bits)] for bits in bit_groups]
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

    qam_signal = np.real(
        signal_symbols * carrier
    )

    return time, qam_signal, bits