import streamlit as st
import base64
import requests
import os
from PIL import Image
import io

# Configuration
OLLAMA_API_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "llava"  # Or "llava-phi", "bakllava", etc.

# Streamlit UI
st.title("🧠 Ollama Vision Object Detection")
st.write("Upload an image to detect objects using the locally running Ollama Vision model.")

uploaded_file = st.file_uploader("Upload an Image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    # ✅ Step 1: Read image bytes
    image_bytes = uploaded_file.read()

    # ✅ Step 2: Load image from bytes (for display)
    image = Image.open(io.BytesIO(image_bytes))
    st.image(image, caption="Uploaded Image", use_container_width=True)

    # ✅ Step 3: Encode to base64 for API
    image_base64 = base64.b64encode(image_bytes).decode("utf-8")

    # ✅ Step 4: Prepare Ollama payload
    payload = {
        "model": MODEL_NAME,
        "prompt": "List all objects detected in this image with their labels and bounding box coordinates.",
        "images": [image_base64],
        "stream": False
    }

    # ✅ Step 5: Send request to Ollama
    st.info("Processing image with Ollama Vision model...")
    response = requests.post(OLLAMA_API_URL, json=payload)

    # ✅ Step 6: Display result
    if response.status_code == 200:
        result = response.json()
        detection_text = result.get("response", "")
        st.success("Detection Results:")
        st.text_area("Output from Vision Model", detection_text, height=300)
    else:
        st.error(f"Error: {response.status_code}")
        st.code(response.text)