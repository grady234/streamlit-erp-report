# app.py
import streamlit as st
import pandas as pd

st.title("ERP Excel Viewer & Chart Demo")
st.write("Upload an Excel file and see its contents and a simple bar chart.")

# File uploader
uploaded_file = st.file_uploader("Choose an Excel file", type=["xlsx"])

if uploaded_file:
    # Read Excel into DataFrame
    df = pd.read_excel(uploaded_file)

    st.subheader("Data Preview")
    st.dataframe(df)  # Show table

    # Check for numeric columns
    numeric_cols = df.select_dtypes('number').columns.tolist()
    if numeric_cols:
        st.subheader("Bar Chart")
        st.bar_chart(df[numeric_cols])
    else:
        st.info("No numeric columns to plot.")
