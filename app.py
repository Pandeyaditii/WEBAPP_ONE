import streamlit as st
from PIL import Image, ImageFilter
import os

# create a floder image
if not os.path.exists('image'):
    os.makedirs('image')

def save_image(image):
         img = Image.open(image)
         img.save(f'image/{image.name}.png')

st.title('🖼️Image Processing App')

upload = st.file_uploader(
       label='upload Your image',
       type=['png','lpg','jpeg']
)
if upload is not None:
       save_image(upload)
       st.image(
              upload,
              caption='Uploaded Image',
              use_column_width=True)