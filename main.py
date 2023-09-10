import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import os


st.title("Automated Exploratory Data Analysis Tool")

uploaded_file = st.file_uploader("Upload File: ")
    

if uploaded_file is not None:
    file_name = uploaded_file.name
    ext = os.path.splitext(file_name)[-1].lower()

    if ext == '.csv':
        df = pd.read_csv(uploaded_file)
    elif ext == '.xlsx':
        df = pd.read_excel(uploaded_file)
    else:
        raise RuntimeError("File extension not recognized")
    
    st.write(df.head())

    df = df.fillna(0)
    st.text("Missing data handled")
    
    column_names = list(df.columns.values)

    for column in column_names:
        df[column] = pd.to_numeric(df[column], errors='coerce')

    st.text("Pre-processing is Complete")

    column = st.selectbox("Choose a column: ", column_names)

    st.text("You selected: " + column)

    if st.button("Visualize Data", type="primary"):
        st.subheader("Line Chart")
        st.line_chart(df[column])

        st.subheader("Bar Chart")
        st.bar_chart(df[column])

        st.subheader("Histogram Chart")
        st.plotly_chart(px.histogram(df))

        st.subheader("Heatmap Chart")
        plot = sns.heatmap(df.corr(), annot=True)
        st.pyplot(plot.get_figure())

