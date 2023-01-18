import streamlit as st 
import pandas as pd, matplotlib as plt
from PIL import Image


st.sidebar.markdown("## Select data to visualize")


# Add a selectbox to the sidebar:
side1_selectbox = st.sidebar.selectbox(
    'Show data by:',
    ('Year', 'Buildings')
)

if side1_selectbox == 'Year':
   side1_slider = st.sidebar.slider(
      "Range of Years", 2013, 2022)
   
   image = Image.open(f'./Graphs/Year/{side1_slider}_Electrical.png')
   st.image(image, caption= "hello", use_column_width = "always")
   # uploadfile = st.file_uploader("Choose image", type="png")
   # if uploadFile is not None:
   #    img = load_image(uploadFile)
   #    st.image(img)
   #    st.write("Image Uploaded Successfully")
   # else:
   #    st.write("Make sure you image is in JPG/PNG Format.")
   
else: 
   side2_selectbox = st.sidebar.selectbox(
      'Choose Building Type',
      ('Academic Buildings', 'North Residence Halls', 'South Residence Hall')
   )
   if side2_selectbox("Academic Buildings"):
      
   