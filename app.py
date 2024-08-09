
import streamlit as st
import pandas as pd
import plotly.express as px

title = "Vehicle Data and Analytics"
print(title.title())

#Introduction: 
# This project uses vehicle data to generate visualizations and analytics that can assist in market research and strategical pricing. 
# The dashboad, includes a histogram displaying the 'most valued' vehicle type based on the sum of prices; and a scatter-plot displaying how an odometer reading can dictate the price of a vehiclie. 

df = pd.read_csv('vehicles_us.csv')

st.header('Vehicle Data and Analytics')

histfig = px.histogram(df, x='type', y='price', title= 'Most Valuable Vehicle Type', labels={'type': 'Vehicle Type', 'price': 'Vehicle Price ($)'})
st.plotly_chart(histfig)

scattfig = px.scatter(df, x='odometer', y='price', title= 'Odometer and Price Correlation', labels= {'odometer': 'Odometer/ Mileage', 'price': 'Vehicle Cost ($)'})
st.plotly_chart(scattfig)

if st.checkbox('Display Scatter Plot'):
    st.plotly_chart(scattfig)

#Conclusion 
# The data displayed within the histogram informs the marketing team that trucks are their most expensive asset with a price sum of over $200M (This does not include pick-ups)
#The scatterplot proves that mileage and price are negatively correlated. As the odometer reading increase, the vehicle price decrease. This is a key metric used to determine vehicle value and appraisal. 