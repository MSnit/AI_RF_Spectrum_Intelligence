import tensorflow as tf
import matplotlib.pyplot as plt
import os

from cnn_model import build_model


IMAGE_SIZE = (224, 224)
BATCH_SIZE = 32


# Load training dataset
train_dataset = tf.keras.utils.image_dataset_from_directory(

    "ai_dataset/train",
    image_size=IMAGE_SIZE,
    batch_size=BATCH_SIZE,

)


# Build model
model = build_model()


# Train model
history = model.fit(

    train_dataset,
    epochs=10,

)


# Create folders
os.makedirs(
    "trained_models",
    exist_ok=True,
)

os.makedirs(
    "results",
    exist_ok=True,
)


# Save model
model.save(

    "trained_models/rf_classifier.keras"

)


# Save accuracy graph
plt.figure()

plt.plot(
    history.history["accuracy"],
    label="Train Accuracy",
)

plt.xlabel("Epoch")
plt.ylabel("Accuracy")
plt.title("CNN Accuracy")
plt.legend()

plt.savefig(
    "results/accuracy_plot.png"
)

plt.close()


# Save loss graph
plt.figure()

plt.plot(
    history.history["loss"],
    label="Train Loss",
)

plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.title("CNN Loss")
plt.legend()

plt.savefig(
    "results/loss_plot.png"
)

plt.close()


print("\nTraining Complete!")