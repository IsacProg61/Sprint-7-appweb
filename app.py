import pandas as pd
import plotly.express as px
import streamlit as st

df = pd.read_csv("vehicles_us.csv")
print(df)

#creation of two columns to have a better user experience

st.header("Car AppWeb")

col1, col2 = st.columns(2)
with col1 :
    """Histogram Button"""
    build_hist = st.checkbox("Build Histogram")

    if build_hist:
        st.write("Histogram of the favorite car colors")
        hist1 = px.histogram(df, x="paint_color")
        st.plotly_chart(hist1, use_container_width=True)

with col2 :
    """Scatter Plot"""
    build_scatter = st.checkbox("Build Scatter")

    if build_scatter :
        st.write("Scatter plot of the diferent prices a car can have")
        scatter = px.scatter(df, x="price",y="type")
        st.plotly_chart(scatter, use_container_width=True)

