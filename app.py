import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('vehicles_us.csv')

st.header('Vehicle Data and Analytics')

histfig = px.histogram(df, x='type', y='price', title= 'Most Valuable Vehicle Type', labels={'type': 'Vehicle Type', 'price': 'Vehicle Price ($)'})
st.plotly_chart(histfig)

scattfig = px.scatter(df, x='odometer', y='price', title= 'Odometer and Price Correlation', labels= {'odometer': 'Odometer/ Mileage', 'price': 'Vehicle Cost ($)'})
st.plotly_chart(scattfig)

if st.checkbox('Display Scatter Plot'):
    st.plotly_chart(scattfig)
