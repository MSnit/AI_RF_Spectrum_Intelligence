from src.communication.bpsk import generate_bpsk_signal

time, signal, bits = generate_bpsk_signal()

print(bits[:20])