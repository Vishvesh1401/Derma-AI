import streamlit as st
import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array

# Load the trained model
model = load_model('best_model.keras')  # Ensure this is the correct path to your model

# Define a function to preprocess the input image
def load_and_preprocess_image(image):
    img = image.resize((224, 224))  # Resize the uploaded image to 224x224
    img = img_to_array(img)  # Convert the resized image to a numpy array
    img = np.expand_dims(img, axis=0)  # Add batch dimension
    img = img / 255.0  # Normalize the image
    return img

# Set the initial theme
st.set_page_config(page_title="Streamlit App with Theme Change", layout="wide")

# Sidebar section
st.sidebar.title("Sidebar Panel")
st.sidebar.header("Input Section")

# Theme selection
theme = st.sidebar.selectbox("Select Theme", ["Light", "Dark"])

# Apply selected theme
if theme == "Light":
    st.markdown("""<style>.main {background-color: #A52A2A; color: white;}</style>""", unsafe_allow_html=True)
else:
    st.markdown("""<style>.main {background-color: #A52A2A; color: black;}</style>""", unsafe_allow_html=True)

# Main section
st.title("Derma AI")
st.header("Use AI to diagnose multiple skin diseases....")

# Section to upload image
st.subheader("Upload an Image")
uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])

# Display the uploaded image and make predictions
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption=f"Uploaded Image - {uploaded_file.name}", use_column_width=True)

    # Preprocess the image for model prediction
    input_data = load_and_preprocess_image(image)
    
    # Make prediction
    prediction = model.predict(input_data)
    predicted_index = np.argmax(prediction)  # Get the index of the class with the highest probability

    # Define your class labels (ensure this matches your trained model classes)
    class_labels = ['Actinic keratosis', 'Atopic Dermatitis', 'Benign Keratosis', 'Dermatofibroma', 'Melanocytic nevus', 'Melanoma', 'Squamous cell carcinoma', 'Tinea Ringworm Candidiasis', 'Vascular lesion']  # Ensure this matches your trained model classes

    # Display predicted class
    if predicted_index < len(class_labels):
        predicted_label = class_labels[predicted_index]
        st.write(f"Predicted Class: {predicted_label}")
    else:
        st.write("Prediction index is out of range.")
