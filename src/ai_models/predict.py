import numpy as np
import tensorflow as tf


CLASS_NAMES = [

    "BPSK",
    "MULTI_TONE",
    "OFDM",
    "QAM",
    "QPSK",

]


model = tf.keras.models.load_model(
    "trained_models/rf_classifier.keras"
)


def predict_signal(image):

    prediction = model.predict(
        image,
        verbose=0,
    )

    index = np.argmax(
        prediction
    )

    confidence = np.max(
        prediction
    ) * 100

    return CLASS_NAMES[index], confidence