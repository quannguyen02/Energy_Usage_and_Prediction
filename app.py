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
   
   if side1_slider == 2013: 
      st.write("In the year 2013,\n\n Electricity usage overall is most from feburary to june and august to december since that is the period students are on campus the most in my perspective. This trend is visible especially for Adam Joseph Lewis Center, Asia House, and Talcott.")
   elif side1_slider == 2014:
      st.write("In the year 2014,\n\n Electricity usage overall is most from feburary to june and august to december since that is the period students are on campus the most in my perspective. There seems to be more use of electricity in Kahn compared to any other residence halls and academic buildings.")
   elif side1_slider == 2015:
      st.write("In the year 2015,\n\n Electricity usage overall is most from feburary to june and august to december since that is the period students are on campus the most in my perspective. This Trend is less visible in Kahn and East since electricity use during the summer is quite high.")
   elif side1_slider == 2016:
      st.write("In the year 2016,\n\n Electricity usage overall is most from feburary to june and august to december since that is the period students are on campus the most in my perspective. In Kohl, electricity usage seems to be similar hroughout the whole year.")
   elif side1_slider == 2017:
      st.write("In the year 2017,\n\n Electricity usage overall is most from feburary to june and august to december since that is the period students are on campus the most in my perspective. There is a high peak during january in Science center. Also, the electricity usage seems to be similar throughout the whole year in Kohl and Science Center.")
   elif side1_slider == 2018:
      st.write("In the year 2018,\n\n Electricity usage overall is most from feburary to june and august to december since that is the period students are on campus the most in my perspective. In Kohl and Science center, electricity usage seems to be similar throughout the year with a peak in september in Science center. Also, the trend is less visible in Kahn, where electricity use during the summer is quite high.")
   elif side1_slider == 2019:
      st.write("In the year 2019,\n\n Electricity usage overall is most from feburary to june and august to december since that is the period students are on campus the most in my perspective. Kohl has a lot of missing data in this year and science center seems to have similar electricity usage throughout the whole year. Also, there is a peak in Asia House in July which seems off from the trend and would be worth looking into the reason for it.")
   elif side1_slider == 2020:
      st.write("In the year 2020,\n\n Electricity usage overall is most from feburary to june and august to december since that is the period students are on campus the most in my perspective. Electricity usage in East has a lot of missing data this year. Science has similar electricity usage throughout the whole year with a slight peak in May. There is less electricity usage in Fairchild during the Fall semester time which is off the trend and worth looking into the reason for this.")
   elif side1_slider == 2021:
      st.write("In the year 2021,\n\n Electricity usage overall is most from feburary to june and august to december since that is the period students are on campus the most in my perspective. There is a significant use of electricity in November. It would be worth looking into the reason behind this peculiar trend to determine what in year 2021 caused this signficant use.")
   elif side1_slider == 2022:
      st.write("In the year 2022,\n\n Electricity usage overall is most from feburary to june and august to december since that is the period students are on campus the most in my perspective. Electricity usage in Kahn and Science Center loos similar throught=out the whole year with a peak in May in Science Center. There is missing data for the whol fall semester time in North and Noah seems to be slightly off trend since electricity usage from september to december is not too differentiable from summer.")

else:
   side2_selectbox = st.sidebar.selectbox("Show prediction for 2023?", ('No', 'Yes'))
   if side2_selectbox == 'No':
      path = './Graphs/Building/'
   else: 
      path = './Graphs/Building_Predict/'

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
         image = Image.open(find(building, path))
         st.image(image)
   
   
   
   # if side2_selectbox("Academic Buildings"):
      
   