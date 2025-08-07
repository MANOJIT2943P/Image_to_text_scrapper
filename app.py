import streamlit as st
import easyocr
import numpy as np
from PIL import Image

st.set_page_config(page_title="OCR App", layout="centered")

st.title("🧠 OCR Text Extractor")
uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

if uploaded_file:
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)

    image = Image.open(uploaded_file)
    image_np = np.array(image)

    with st.spinner("Extracting text..."):
        reader = easyocr.Reader(['en'])
        results = reader.readtext(image_np)
        
        
    scraped_text=""
    st.success("✅ Text extracted:")
    for (bbox, text, prob) in results:
        scraped_text+=text
    text=scraped_text.split('*')
    
    for t in text:
        st.markdown(f"{t}")
