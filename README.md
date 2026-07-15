# AI-Powered RF Spectrum Intelligence Platform

An AI-based RF signal analysis and communication signal classification platform that combines Digital Signal Processing (DSP), spectrogram-based feature extraction, and Convolutional Neural Networks (CNNs) for automatic signal identification.

---

## Project Overview

The AI-Powered RF Spectrum Intelligence Platform is designed to generate, process, analyze, and classify RF communication signals using modern signal processing and machine learning techniques.

The platform provides an interactive Streamlit dashboard for:

- RF signal generation
- Signal processing and filtering
- FFT-based frequency analysis
- Spectrogram generation
- AI-based signal classification
- Communication signal visualization

The project demonstrates the integration of:

- Digital Signal Processing (DSP)
- Communication Systems
- Machine Learning
- RF Signal Analysis
- Interactive Dashboard Development

---

## Features

### Communication Signals Supported

- Multi-Tone Signal
- BPSK (Binary Phase Shift Keying)
- QPSK (Quadrature Phase Shift Keying)
- 16-QAM (Quadrature Amplitude Modulation)
- OFDM (Orthogonal Frequency Division Multiplexing)

---

### Signal Processing Features

- Additive White Gaussian Noise (AWGN)
- Low Pass Digital Filtering
- Fast Fourier Transform (FFT)
- Spectrogram Generation
- Frequency Spectrum Analysis

---

### AI Features

- Automatic Dataset Generation
- Spectrogram-based Feature Extraction
- CNN Model Training
- RF Signal Classification
- Confidence Score Prediction

---

### Dashboard Features

The Streamlit dashboard provides:

- Signal Configuration
- Signal Type Selection
- Noise Control
- Filter Configuration
- Time Domain Visualization
- Frequency Domain Visualization
- Spectrogram Visualization
- AI Prediction Module
- Confidence Score Display

---

## Project Architecture

```
User Input
    |
    v
Signal Generation
    |
    v
Noise Addition
    |
    v
Digital Filtering
    |
    v
FFT Processing
    |
    v
Spectrogram Generation
    |
    v
Dataset Generation
    |
    v
CNN Model Training
    |
    v
Signal Classification
    |
    v
AI Prediction
    |
    v
Streamlit Dashboard
```

---

## Folder Structure

```
AI_RF_SPECTRUM_INTELLIGENCE/

├── app.py
├── main.py
├── config.py
├── README.md
├── requirements.txt

├── ai_dataset/
│   ├── train/
│   ├── validation/
│   └── test/

├── datasets/
├── trained_models/
├── results/

├── src/
│
├── ai_models/
├── communication/
├── datasets/
├── feature_extraction/
├── filters/
├── noise/
├── pipeline/
├── signal_generation/
├── signal_processing/
└── visualization/

```

---

## Technologies Used

| Technology | Usage |
|-----------|-----------|
| Python | Core Development |
| Streamlit | Dashboard |
| TensorFlow | CNN Training |
| NumPy | Numerical Computing |
| Matplotlib | Visualization |
| SciPy | Signal Processing |
| PIL | Image Processing |
| Git | Version Control |

---

## Dataset Generation

The platform automatically generates spectrogram images for communication signals.

Supported classes:

- BPSK
- QPSK
- QAM
- OFDM
- MULTI_TONE

Dataset structure:

```
ai_dataset/

train/
validation/
test/
```

---

## AI Model

The project uses a Convolutional Neural Network (CNN) for communication signal classification.

CNN Workflow:

```
Spectrogram Image
        |
        v
Convolution Layer
        |
        v
Pooling Layer
        |
        v
Flatten Layer
        |
        v
Dense Layer
        |
        v
Softmax Layer
        |
        v
Predicted Signal Class
```

Output classes:

```
BPSK
QPSK
QAM
OFDM
MULTI_TONE
```

---

## Running the Dashboard

Install the dependencies:

```bash
pip install -r requirements.txt
```

Run the Streamlit dashboard:

```bash
streamlit run app.py
```

---

## Generating the Dataset

Run:

```bash
python generate_ai_dataset.py
```

---

## Training the CNN Model

Run:

```bash
python src/ai_models/train_model.py
```

The trained model is stored in:

```
trained_models/
```

---

## AI Prediction

The trained CNN model predicts:

- Signal Type
- Confidence Score

Example:

```
Detected Signal : QPSK

Confidence Score : 94.27%
```

---

## Results

The project generates:

- Accuracy Plot
- Loss Plot
- Trained CNN Model
- Spectrogram Images
- AI Predictions

Generated files are stored in:

```
results/
```

---

## Applications

- RF Spectrum Monitoring
- Communication Signal Analysis
- AI-based Signal Classification
- Educational DSP Projects
- Wireless Communication Research
- Machine Learning for Signal Processing

---

## Future Improvements

Possible future enhancements:

- SDR Hardware Integration
- Additional Modulation Schemes
- Real-time RF Signal Classification
- Advanced Deep Learning Models
- Signal Detection in Noisy Environments

---

## Author

**Manthan Sontakke**

B.Tech Electronics and Communication Engineering (Artificial Intelligence and Cybernetics)

VIT Bhopal University

GitHub: https://github.com/MSnit

---

## Version

```
Version 1.0
```

Project Status:

```
Implementation Complete
```
