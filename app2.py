import streamlit as st 
import pandas as pd, matplotlib as plt
from PIL import Image
import os

@st.cache
# find the file
def find(name, path):
    for file in os.listdir(path):
        if name in file:
            return path + file


st.set_page_config(layout="wide")
st.sidebar.markdown("# Select data to visualize")

# Add a selectbox to the sidebar:
side1_selectbox = st.sidebar.selectbox(
    'Show data by:',
    ('Year', 'Buildings')
) 

if side1_selectbox == 'Year':
   # multiselect_year = st.sidebar.multiselect("Choose Year(s) to display", range(2013,2023))
   
   side1_slider = st.sidebar.slider(
      "Range of Years", 2013, 2022)
   
   image = Image.open(f'./Graphs/Year/{side1_slider}_Electrical.png')
   st.image(image, use_column_width = True)
   
else:
   side2_selectbox = st.sidebar.multiselect(
      'Choose Academic Buildings',
      ['Adam Joseph Lewis Center', 'Kohl Building', 'Science Center']
   )
   
   side3_selectbox = st.sidebar.multiselect(
      'Choose North Residence Halls',
      ['Asia House', 'East', 'Kahn', 'North', 'Noah']
   )
   side4_selectbox = st.sidebar.multiselect(
      'Choose South Residence Halls',
      ['Fairchild', 'Harvey', 'Lord-Saunders', 'Talcott']
   )
   for box in [side2_selectbox, side3_selectbox, side4_selectbox]:
      for building in box:
         image = Image.open(find(building, './Graphs/Building/'))
         st.image(image)
   
   
   
   # if side2_selectbox("Academic Buildings"):
      
   