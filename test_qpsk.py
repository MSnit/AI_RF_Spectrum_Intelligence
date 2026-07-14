from src.communication.qpsk import generate_qpsk_signal

time, signal, bits = generate_qpsk_signal()

print(bits[:20])