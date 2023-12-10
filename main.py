import streamlit as st
import cv2     # image processing
import numpy as np # numerical processing
from PIL import Image # image processing
from PIL import ImageDraw, ImageFont
import matplotlib.pyplot as plt # plotting 

# Config
st.set_page_config(
    layout="centered",
    page_title="Image Manipulation App",
    page_icon="📸",
    initial_sidebar_state='expanded',

)

with st.container():
    st.title(':rainbow[Image Manipulation App]')
    


uploaded_file = st.file_uploader("Choose a image file", type="jpg")


with st.spinner('Processing Image'):
    if uploaded_file is not None:
        # Convert the file to an opencv image.
        open_image=Image.open(uploaded_file)
        
        #  let's display the image:
        st.image(open_image,caption='Original Image')



st.subheader('Resize the image',divider='blue')
c1,c2=st.columns(2)
#Resize
if c1.button('Resize'): 
 ht = st.number_input('Enter the height of image: ',placeholder='Type a number',value=None)
 wd = st.number_input('Enter the width of image: ', placeholder='Type a Number',value=None)
 Resized=open_image.resize((ht,wd))
 c2.image(Resized)


#Color change
st.subheader('Convert the color of the image',divider='rainbow')

c1,c2=st.columns(2)
if c1.button('Gray'):
        im=cv2.imread(uploaded_file)
        cats_color_grey=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
        plt.imshow(cats_color_grey,cmap='gray')
        plt.axis('off')


st.subheader('Rotate the image',divider='blue')

c1,c2=st.columns(2)
if c1.button('Rotate left'):
    Ri=open_image.rotate(90,expand=True)
    st.image(Ri)
if c1.button('Rotate Right'):
    Ri=open_image.rotate(-90,expand=True)
    st.image(Ri)
if c1.button('Invert'):
    Ri =open_image.rotate(180,expand=True)
    st.image(Ri)


