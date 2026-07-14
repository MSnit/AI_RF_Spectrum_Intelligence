"""
dataset_generator.py

Automatic RF dataset generation.
"""

import os
import random
import matplotlib.pyplot as plt

from src.pipeline.rf_pipeline import run_pipeline
from src.feature_extraction.spectrogram import plot_spectrogram


def generate_dataset(
    output_folder,
    number_of_samples,
):
    """
    Generate spectrogram images for AI training.
    """

    os.makedirs(output_folder, exist_ok=True)

    for i in range(number_of_samples):

        frequencies = [
            random.randint(500, 1500),
            random.randint(1600, 2800),
            random.randint(3000, 4500),
        ]

        amplitudes = [1.0, 0.7, 0.5]

        results = run_pipeline(
            frequencies=frequencies,
            amplitudes=amplitudes,
            noise_std=random.uniform(0.0, 0.5),
            cutoff_frequency=2500,
        )

        fig = plot_spectrogram(
            results["filtered_signal"],
            10000,
        )

        filename = os.path.join(
            output_folder,
            f"spectrogram_{i:04d}.png",
        )

        fig.savefig(filename)


        plt.close(fig)