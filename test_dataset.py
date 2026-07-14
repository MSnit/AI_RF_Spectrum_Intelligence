from src.datasets.dataset_generator import generate_dataset

generate_dataset(
    output_folder="datasets/train/unknown",
    number_of_samples=10,
)

print("Dataset generation completed successfully!")
