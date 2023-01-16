import streamlit as st
import numpy as np
import pandas as pd
import time

#1
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)

#2
x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)

#3
st.text_input("Your name", key="name")

# You can access the value at any point with:
st.session_state.name

#4
@st.cache
def chartData():
   return pd.DataFrame(
      np.random.randn(20, 3),
      columns=['a', 'b', 'c'])
    
if st.checkbox('Show dataframe'):
   chart_data = chartData()
   chart_data
   
#5
import pandas as pd

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
    })

option = st.selectbox(
    'Which number do you like best?',
     df['first column'])

'You selected: ', option

#6
# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

# Add a slider to the sidebar:
add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)

#7
left_column, right_column = st.columns(2)
# You can use a column just like st.sidebar:
left_column.button('Press me!')

# Or even better, call Streamlit functions inside a "with" block:
with right_column:
    chosen = st.radio(
        'Sorting hat',
        ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
    st.write(f"You are in {chosen} house!")
    
#8
#7
side_left_column, side_right_column = st.sidebar.columns(2)
# You can use a column just like st.sidebar:
side_left_column.button('Press me1!')

# Or even better, call Streamlit functions inside a "with" block:
with side_right_column:
    chosen = st.radio(
        '1Sorting hat',
        ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
    st.write(f"1You are in {chosen} house!")
    
#9
'Starting a long computation...'

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(1
             )

'...and now we\'re done!'