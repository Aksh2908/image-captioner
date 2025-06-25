import streamlit as st
import os
from PIL import Image
import generate

st.set_page_config(page_title="Image Caption Generator", layout="centered")

st.title("🖼️ Image Caption Generator")
st.markdown("Upload an image and generate a caption using a deep learning model.")

uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])

# If an image is uploaded
if uploaded_file is not None:
    # Save the file temporarily
    temp_path = os.path.join("temp_image.jpg")
    with open(temp_path, "wb") as f:
        f.write(uploaded_file.read())

    # Display image
    image = Image.open(temp_path)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Generate caption
    if st.button("🧠 Generate Caption"):
        with st.spinner("Generating caption..."):
            caption = generate.runModel(temp_path)
        st.success("✅ Caption Generated!")
        st.markdown(f"**📝 Caption:** {caption}")
