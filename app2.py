import streamlit as st 
import pandas as pd, matplotlib as plt

st.sidebar.markdown("## Select data to visualize")
st.sidebar

# Add a selectbox to the sidebar:
side1_selectbox = st.sidebar.selectbox(
    'Show data by:',
    ('Year', 'Buildings')
)

if side1_selectbox == 'Year':
   side1_slider = st.sidebar.slider(range(2013,2023))
else: 
   side2_selectbox = st.sidebar.selectbox(
      'Choose Building Type',
      ('Academic Buildings', 'North Residence Halls', 'South Residence Hall')
   )
   if side2_selectbox("Academic Buildings"):
      
   