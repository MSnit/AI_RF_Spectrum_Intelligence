from src.communication.qam import generate_qam_signal

time, signal, bits = generate_qam_signal()

print(bits[:20])