from src.datasets.dataset_generator import (
    generate_dataset,
)


# Training Dataset

generate_dataset(
    signal_type="BPSK",
    output_folder="ai_dataset/train/BPSK",
    number_of_samples=10,
)

generate_dataset(
    signal_type="QPSK",
    output_folder="ai_dataset/train/QPSK",
    number_of_samples=10,
)

generate_dataset(
    signal_type="QAM",
    output_folder="ai_dataset/train/QAM",
    number_of_samples=10,
)

generate_dataset(
    signal_type="OFDM",
    output_folder="ai_dataset/train/OFDM",
    number_of_samples=10,
)

generate_dataset(
    signal_type="MULTI_TONE",
    output_folder="ai_dataset/train/MULTI_TONE",
    number_of_samples=10,
)


print("\nDataset Generated Successfully!")