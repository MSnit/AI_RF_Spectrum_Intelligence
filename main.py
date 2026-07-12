from src.signal_generation.signal_generator import generate_sine_wave

# Generate a 1 kHz sine wave
time, signal = generate_sine_wave(
    frequency=1000,
    amplitude=1,
    sampling_rate=10000,
    duration=1
)

print("First 10 Time Samples:")
print(time[:10])

print()

print("First 10 Signal Samples:")
print(signal[:10])
