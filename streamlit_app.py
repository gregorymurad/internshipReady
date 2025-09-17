import streamlit as st
import pandas as pd
import plotly.express as px


st.set_page_config(page_title="Dashboard",
                   layout="wide")

st.title("Water Quality Dashboard")
st.header("CIS 3590 - Internship Ready Software Development")
st.subheader("Prof. Gregory Murad Reis")

st.sidebar.title("File Upload")

uploaded_file = st.sidebar.file_uploader("Choose a file", type=["csv"])
st.sidebar.info("If no CSV file is uploaded, a default one will be used.")

# st.success("It worked :)")
# st.warning("Almost there! Try again")
# st.error("Sorry, it didn't work this time")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
else:
    df = pd.read_csv("biscayne_bay_dataset_oct_2022.csv")

st.divider()

tables, scatterPlot, maps, threeDPlot = st.tabs([
    "Tables",
    "Correlation",
    "Maps",
    "3d Visualization"
])

with tables:
    st.write("Raw Data")
    st.dataframe(df)
    st.write("Descriptive Statistics")
    st.dataframe(df.describe())

with scatterPlot:
    st.write("Correlation")
    fig1 = px.scatter(df,
                      x="Temperature (C)",
                      y="Total Water Column (m)",
                      color="pH")
    st.plotly_chart(fig1)

with maps:
    st.write("Map")
    fig2 = px.scatter_mapbox(df,
                             lat="latitude",
                             lon="longitude",
                             zoom=17,
                             mapbox_style="open-street-map",
                             hover_data=df,
                             color="Temperature (C)")
    st.plotly_chart(fig2)

with threeDPlot:
    st.write("3d Visualization")
    fig3 = px.scatter_3d(df,
                         x="longitude",
                         y="latitude",
                         z="Total Water Column (m)",
                         color="Temperature (C)",)
    fig3.update_scenes(zaxis_autorange="reversed")
    st.plotly_chart(fig3)