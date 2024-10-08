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

hist = px.histogram(vehicles_us, x='manufacturer', y='price', title='Price distribution of cars based on the manufacturers', labels={'manufacturer': 'Manufacturer', 'price': 'Price'}) 
st.plotly_chart(hist)


veh_scatter = px.scatter(vehicles_us, x='cylinders', y='price', title='Price based on the cylinders in a car', labels={'cylinders': 'Cylinders', 'price': 'Price'})
st.plotly_chart(veh_scatter)

fig_scatter = px.scatter(vehicles_us, x='odometer', y='price', title='Price vs Odometer', labels={'odometer': 'Odometer', 'price': 'Price'})
st.plotly_chart(fig_scatter)

scatter = px.scatter(vehicles_us, x='model_year', y='price', title='Price based on the model year of a car', labels={'model_year': 'Model Year', 'price': 'Price'})
st.plotly_chart(scatter)

us_scatter = px.scatter(vehicles_us, x='days_listed', y='price', title='Price based on the day the car is listed', labels={'days_listed': 'Days listed', 'price': 'Price'})
st.plotly_chart(us_scatter)

veh = px.scatter(vehicles_us, x='model_year', y='odometer', title='Odometer reading based on the model year of a car', labels={'model_year': 'Model Year', 'odometer': 'Odometer'})
st.plotly_chart(veh)

if st.checkbox('Show Histogram'):
    st.plotly_chart(veh_hist)
    st.plotly_chart(fig_hist)
    st.plotly_chart(hist)


if st.checkbox('Show Scatter Plot'):
    st.plotly_chart(veh_scatter)
    st.plotly_chart(fig_scatter)
    st.plotly_chart(scatter)
    st.plotly_chart(us_scatter)
    st.plotly_chart(veh)