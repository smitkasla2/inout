import streamlit as st
from PIL import Image

def main():
    st.title("Image Size Checker")

    uploaded_image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    if uploaded_image is not None:
        image = Image.open(uploaded_image)
        width, height = image.size
        st.write(f"Image size: {width}x{height}")

if __name__ == "__main__":
    main()
