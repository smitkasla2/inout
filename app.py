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
            # Replace placeholder in size.ipynb with actual image string
            size_nb_content = '''
            # Check Image Size
            import io
            from PIL import Image
            import base64

            # Convert base64 string to bytes
            img_bytes = io.BytesIO(base64.b64decode('{0}'))
            image = Image.open(img_bytes)

            # Get and print image size
            size = image.size
            size
            '''.format(img_str)

            # Pass modified content to IPython Notebook
            result = st.write(size_nb_content, format='ipynb')

            # Display result from size.ipynb
            st.write("Image Size:", result)

if __name__ == "__main__":
    main()
