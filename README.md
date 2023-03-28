# Visualize Oberlin College's Energy Usage and Prediction
Authors: Quan Nguyen, Emma Lee
Date: Jan 18th, 2023

Electricity Data for Oberlin College's Dorms and Buildings collected from Oberlin Environmental Dashboard: https://environmentaldashboard.org

Preprocess.py: preprocess 10 years of collected data by days and statistically removed outliers.
MakePlots.ipynb: 
    - Categorize data to their corresponding building types, including South and North Dorms and Academic Buildings.
    - Plot visualization by building types and years.
Train&Predict.ipynb: 
    - Train and predict 2023-2024 trend for energy usage using Long Short-Term Memory Model and plot the result.
app.py:
    - Create a website using Streamlit to display the visualizations and predictions.

Data: contains raw energy data and preprocessed data

Graphs: contains visualization plots
Weight and training_1: contains information on the LSTM model

Get the requirements:
```
pip3 install -r requirements.txt
```

Run the website application:
```
streamlit run app.py
```
