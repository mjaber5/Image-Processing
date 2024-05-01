import streamlit as st
import numpy as np
from PIL import Image
from image_processor import ImageProcessor

def load_image(image_file):
    img = Image.open(image_file)
    return img

def display_image(image, caption="Image"):
    st.image(image, caption=caption, use_column_width=True)

def process_image(image, operation_type):
    processor = ImageProcessor()
    cv_image = np.array(image.convert('RGB'))
    processed_image = processor.process(cv_image, operation_type)
    return Image.fromarray(processed_image)

def main():
    st.title('Image Processing App')
    image_file = st.file_uploader("Upload Images", type=["png", "jpg", "jpeg"])
    if image_file is not None:
        image = load_image(image_file)
        display_image(image, "Uploaded Image")
        operation = st.selectbox("Choose an operation", ('Erosion', 'Dilation', 'Opening', 'Closing'))
        if st.button('Process Image'):
            processed_image = process_image(image, operation.lower())
            display_image(processed_image, "Processed Image")

if __name__ == "__main__":
    main()
