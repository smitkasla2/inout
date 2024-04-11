import streamlit as st
from PIL import Image
import io
import base64

def main():
    st.title("Image Size Checker")

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        # Convert image to bytes
        img_bytes = io.BytesIO()
        image.save(img_bytes, format='PNG')
        img_str = base64.b64encode(img_bytes.getvalue()).decode('utf-8')

        if st.button("Check Size"):
            # Pass image to IPython Notebook
            result = st.write('''
            # Check Image Size
            import io
            from PIL import Image
            import base64

            # Convert base64 string to bytes
            img_bytes = io.BytesIO(base64.b64decode('{}'))
            image = Image.open(img_bytes)

            # Get image size
            size = image.size
            size
            '''.format(img_str), format='ipynb')

            # Display result from size.ipynb
            with st.echo():
                size_result = st.capture_output(result)
                st.write("Image Size:", size_result)

if __name__ == "__main__":
    main()
