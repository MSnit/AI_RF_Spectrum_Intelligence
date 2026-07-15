from src.communication.ofdm import generate_ofdm_signal

time, signal = generate_ofdm_signal()

print(signal[:10])