import os
import random
import matplotlib.pyplot as plt

from src.pipeline.rf_pipeline import run_pipeline
from src.feature_extraction.spectrogram import (
    plot_spectrogram,
)


def generate_dataset(

        signal_type,
        output_folder,
        number_of_samples,

):

    os.makedirs(
        output_folder,
        exist_ok=True,
    )

    for i in range(number_of_samples):

        results = run_pipeline(

            signal_type=signal_type,
            noise_std=random.uniform(
                0.0,
                0.5,
            ),
            cutoff_frequency=2500,
            frequencies=[1000, 2000, 3500],
            amplitudes=[1.0, 0.5, 0.8],

        )

        fig = plot_spectrogram(

            results["filtered_signal"],
            10000,

        )

        filename = os.path.join(

            output_folder,
            f"{signal_type}_{i:04d}.png",

        )

        fig.savefig(filename)

        plt.close(fig)