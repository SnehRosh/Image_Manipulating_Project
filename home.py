import streamlit as st
import numpy as np # numerical processing
from PIL import Image # image processing
from PIL import ImageDraw, ImageFont, ImageFilter, ImageEnhance
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


if uploaded_file is None:
     print('Please upload the file')
elif uploaded_file is not None:
    # Convert the file to an opencv image.
    open_image=Image.open(uploaded_file)
    #  let's display the image:
    st.image(open_image,caption='Original Image')

   

actions = {}


#Resize
st.subheader('Resize the image',divider='blue')
c1,c2=st.columns(2) 
f = c1.form('resize')
ht = f.number_input('Enter the height of image: ',placeholder='Type a number',value=0)
wd = f.number_input('Enter the width of image: ', placeholder='Type a Number',value=0)
btn = f.form_submit_button("Resize")
if btn and isinstance(ht, (int,float)) and isinstance(wd, (int, float)):
    Resized=open_image.resize((ht,wd))
    c2.image(Resized)
    Resized.save('Resized.png')
    btn = st.download_button(
            label="Download image",
            data=open('Resized.png', 'rb').read(),
            file_name="Resized_image.png",
            mime="image/png"
            )
else:
    c2.info("Please enter numeric values")


    

#Color change
st.subheader('Convert the color of the image',divider='rainbow')

c1,c2=st.columns(2)
f=c1.form('Filter Image')
filter_options = ['Outline','Inverted oulined','Emboss','Blur','Min_Filter','Sharpen','Smooth']
filter = c1.radio("apply an image filter",filter_options)
f_image = open_image
if filter == filter_options[0]:
    f_image = open_image.filter(ImageFilter.CONTOUR)
if filter == filter_options[1]:
    f_image = open_image.filter(ImageFilter.FIND_EDGES)
if filter == filter_options[2]:
    f_image = open_image.filter(ImageFilter.EMBOSS)
if filter == filter_options[3]:
    f_image = open_image.filter(ImageFilter.BLUR)   
if filter == filter_options[4]:
    f_image = open_image.filter(ImageFilter.MinFilter(3)) 
if filter == filter_options[5]:
    f_image = open_image.filter(ImageFilter.SHARPEN) 
if filter == filter_options[6]:
    f_image = open_image.filter(ImageFilter.SMOOTH)          
c2.image(f_image)
btn = f.form_submit_button(":red[Click here to get download button]") 
if btn:    
    f_image.save('Filtered.png')
    btn = st.download_button(
        label="Download image",
        data=open('Filtered.png', 'rb').read(),
        file_name="Filtered_image.png",
        mime="image/png"
        )

#Rotate
st.subheader('Rotate the image',divider='blue')

c1,c2=st.columns(2)
f = c1.form('Rotate')
rotate_options = ['Right','Left','Invert','Original']
rotate = c1.radio("apply an image filter",rotate_options)
if rotate==rotate_options[0]:
    Ri=open_image.rotate(90,expand=True)  

if rotate==rotate_options[1]:
    Ri=open_image.rotate(-90,expand=True)

if rotate==rotate_options[2]:
    Ri =open_image.rotate(180,expand=True)
 
if rotate==rotate_options[3]:
    Ri=open_image
c2.image(Ri)
btn = f.form_submit_button(":red[Click here to get download button]") 
if btn:    
    Ri.save('Oriented.png')
    btn = st.download_button(
        label="Download image",
        data=open('Oriented.png', 'rb').read(),
        file_name="Oriented_image.png",
        mime="image/png"
        )

    
    
#crop
st.subheader('Crop the image',divider='blue')

c1,c2=st.columns(2)
f = c1.form('Crop')
lft = f.number_input('Left: ',placeholder='Type a number',value=0)
upr = f.number_input('Upper: ',placeholder='Type a number',value=0)
rgt = f.number_input('Right: ', placeholder='Type a Number',value=0)
lwr = f.number_input('Lower: ', placeholder='Type a Number',value=0)
btn = f.form_submit_button("Crop")
if btn and isinstance(lft, (int,float)) and isinstance(rgt, (int, float)) and isinstance(upr, (int, float)) and isinstance(lwr, (int, float)):
    Cropped=open_image.crop((lft,upr,rgt,lwr))
    c2.image(Cropped)
    Cropped.save('Cropped.png')
    btn = st.download_button(
            label="Download image",
            data=open('Cropped.png', 'rb').read(),
            file_name="Cropped_image.png",
            mime="image/png"
            )
else:
    c2.info("Please enter numeric values")