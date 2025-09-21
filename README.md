# 🩺 Derma AI

Derma AI is a **Streamlit-based web application** that uses a trained deep learning model to assist in diagnosing multiple skin diseases from uploaded images.


## 🚀 Features

* Upload an image (`.jpg`, `.jpeg`, `.png`) of a skin lesion.
* AI-powered predictions using a trained TensorFlow/Keras model.
* Supports multiple skin disease classes:

  * Actinic keratosis
  * Atopic Dermatitis
  * Benign Keratosis
  * Dermatofibroma
  * Melanocytic nevus
  * Melanoma
  * Squamous cell carcinoma
  * Tinea Ringworm Candidiasis
  * Vascular lesion
* Light/Dark theme toggle.



## 📂 Project Structure


├── front_end.py        # Streamlit app
├── best_model.keras    # Trained deep learning model (not included in repo)
├── requirements.txt    # Dependencies
└── README.md           # Documentation


## ⚙️ Installation

1. Clone the repository:

   git clone https://github.com/your-username/derma-ai.git
   cd derma-ai

2. Install dependencies:

   pip install -r requirements.txt
 

   *(or install manually: `streamlit tensorflow pillow numpy kagglehub`)*

3. Ensure you have your trained model file:

## 🔗 Model Download

The trained model `best_model.keras` is too large to upload to GitHub.  
You can download it from Google Drive using this link:  
[Download the model]()

Place the file in the project root directory before running the app.

## ▶️ Usage

Run the Streamlit app:

```bash
streamlit run front_end.py
```

Then open your browser at `http://localhost:8501`.

---

## 📊 Example

Upload an image of a skin lesion, and the app will display:

* The uploaded image
* The predicted disease class

---

## 📂 Dataset

The model was trained on the **Skin Disease Classification Image Dataset** available on Kaggle.

To download the dataset using [KaggleHub](https://pypi.org/project/kagglehub/):

```python
import kagglehub

# Download latest version of the dataset
path = kagglehub.dataset_download("riyaelizashaju/skin-disease-classification-image-dataset")

print("Path to dataset files:", path)
```

> ⚠️ Note: The dataset is **only required if you want to re-train the model**.
> For running the app with the provided `best_model.keras`, you do **not** need the dataset.

---

## 🛠️ Requirements

* Python 3.8+
* Streamlit
* TensorFlow / Keras
* Pillow
* NumPy
* KaggleHub (for dataset download)

---

## ⚠️ Disclaimer

This application is for **educational and research purposes only**. It is **not a substitute for professional medical advice**. Always consult a qualified dermatologist for medical concerns.

---

