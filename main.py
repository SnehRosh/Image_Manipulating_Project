import streamlit as st
import cv2     # image processing
import numpy as np # numerical processing
from PIL import Image # image processing
import matplotlib.pyplot as plt # plotting 

# Config
st.set_page_config(
    layout="centered",
    page_title="Image Manipulation App",
    page_icon="📸",
    initial_sidebar_state='expanded',

)

uploaded_file = st.file_uploader("Choose a image file", type="jpg")

with st.spinner('Processing Immigration Data'):
    if uploaded_file is not None:
        # Convert the file to an opencv image.
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        opencv_image = cv2.imdecode(file_bytes, 1)

        #  let's display the image:
        st.image(opencv_image, channels="BGR")

#Resize
if st.button('Resize'):
    new_image = Image.open(uploaded_file)
    ht = st.number_input('Enter the height of image: ')
    wd = st.number_input('Enter the width of image: ')
    new_image.resize((ht,wd))



