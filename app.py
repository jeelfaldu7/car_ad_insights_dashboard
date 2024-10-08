import streamlit as st
import pandas as pd
import plotly.express as px

vehicles_us = pd.read_csv('vehicles_us.csv')

st.write(vehicles_us)
st.header('Software Development Tool Application')

vehicles_us['price'] = pd.to_numeric(vehicles_us['price'], errors='coerce').fillna(0).astype('int64')

vehicles_us['manufacturer'] = vehicles_us['model'].str.split().str[0]

manufacturer_type_counts = vehicles_us.groupby(['manufacturer', 'type']).size().reset_index(name='count')

veh_hist = px.histogram(manufacturer_type_counts, x='manufacturer', color='type', title='Vehicle types by manufacturer', labels={'manufacturer': 'Manufacturer', 'type': 'Vehicle Type'}) 
st.plotly_chart(veh_hist)

fig_hist = px.histogram(vehicles_us, x='model_year', color='condition', title='Condition vs Model Year', labels={'model_year': 'Model Year', 'condition': 'Condition'}) 
st.plotly_chart(fig_hist)

hist = px.histogram(vehicles_us, x='price', y='manufacturer', title='Price distribution of cars based on the manufacturers', labels={'price': 'Price', 'manufacturer': 'Manufacturer'}) 
st.plotly_chart(hist)


veh_scatter = px.scatter(vehicles_us, x='cylinders', y='price', title='Price based on the cylinders in a car', labels={'cylinders': 'Cylinders', 'price': 'Price'})
st.plotly_chart(veh_scatter)

if st.checkbox('Show Histogram'):
    st.plotly_chart(veh_hist)
    st.plotly_chart(fig_hist)
    st.plotly_chart(hist)


if st.checkbox('Show Scatter Plot'):
    st.plotly_chart(veh_scatter)
