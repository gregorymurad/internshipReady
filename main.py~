import streamlit as st
import plotly.express as px
import pandas as pd

st.set_page_config(page_title="Dashboard",
                   layout="wide")

st.title("Water Quality Data Dashboard")
st.subheader("Visualization Tool for Biscayne Bay Water Quality using Aquatic Robots")

uploaded_file = st.sidebar.file_uploader("Choose a csv file")
st.sidebar.info("If no CSV file is uploaded, a default one will be displayed.")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
else:
    df = pd.read_csv("biscayne_bay_dataset_oct_2021-1.csv")

maps, linePlot, scatterPlot, threeDPlot, tables = st.tabs([
    "Interactive Map",
    "Line Chart",
    "Correlation",
    "3D Chart",
    "Tables"
])

with scatterPlot:
    st.subheader("Scatter Plots for the Water Parameters")
    fig = px.scatter(df,
                     x="Salinity (ppt)",
                     y="Temperature (C)",
                     color = "ODO (mg/L)")
    st.plotly_chart(fig)

with linePlot:
    st.subheader("Line Chart")

    col1, col2 = st.columns([2,5])
    with col1:
        color = st.color_picker("Choose a color","#081E3F")
    with col2:
        fig2 = px.line(df,
                       x=df.index,
                       y="ODO (mg/L)")
        fig2.update_traces(line_color=color)
        st.plotly_chart(fig2)

with maps:
    st.subheader("Maps")
    fig3 = px.scatter_mapbox(df,
                             lat="latitude",
                             lon="longitude",
                             mapbox_style="open-street-map",
                             zoom=17,
                             hover_data=df)
    st.plotly_chart(fig3)

with threeDPlot:
    st.subheader("3D Visualization")
    fig4 = px.scatter_3d(df,
                         x="longitude",
                         y="latitude",
                         z="Total Water Column (m)")
    fig4.update_scenes(zaxis_autorange="reversed")
    st.plotly_chart(fig4)

with tables:
    st.subheader("Raw Data")
    st.dataframe(df)
    st.divider()
    st.subheader("Descriptive Statistics")
    st.dataframe(df.describe())
