import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('vehicles_us.csv')

st.write(df.head())
st.header('Software Development Tool Application')

veh_hist = px.histogram(df, x='price')  # Replace 'column_name' with the column you want to plot
st.plotly_chart(veh_hist)

veh_scatter = px.scatter(df, x='type', y='price')  # Replace 'x_column' and 'y_column' with actual column names
st.plotly_chart(veh_scatter)

if st.checkbox('Show Histogram'):
    st.plotly_chart(veh_hist)

if st.checkbox('Show Scatter Plot'):
    st.plotly_chart(veh_scatter)
