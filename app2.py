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
   side1_slider = st.sidebar.slider()

else: 
   # side2_selectbox = st.sidebar.selectbox(
   #    'Choose Building Type',
   #    ('Academic Buildings', 'North Residence Halls', 'South Residence Hall')
   # )
   # if side2_selectbox("Academic Buildings"):
   year = 2013
   image = Image.open(f'./Graphs/Year/{year}_Electrical.png')
   st.write(image)