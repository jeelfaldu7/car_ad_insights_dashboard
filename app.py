import streamlit as st
import pandas as pd
import plotly.express as px

vehicles_us = pd.read_csv('vehicles_us.csv')

st.write(vehicles_us.head())
st.header('Software Development Tool Application')

vehicles_us['price'] = pd.to_numeric(vehicles_us['price'], errors='coerce').fillna(0).astype('int64')

veh_hist = px.histogram(vehicles_us, x='price')  # Replace 'column_name' with the column you want to plot
st.plotly_chart(veh_hist)

veh_scatter = px.scatter(vehicles_us, x='type', y='price')  # Replace 'x_column' and 'y_column' with actual column names
st.plotly_chart(veh_scatter)

if st.checkbox('Show Histogram'):
    st.plotly_chart(veh_hist)

if st.checkbox('Show Scatter Plot'):
    st.plotly_chart(veh_scatter)
