#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  6 11:07:50 2025

@author: gradyjurrens
"""

# save this as app.py

import streamlit as st
import pandas as pd
from io import BytesIO

# Title of the app
st.title("Monthly Sales Report Generator")

st.write("Click the button below to generate an Excel report with a chart.")

# Input fields (optional)
customer = st.text_input("Customer Name", "All Customers")

# Button to trigger the report
if st.button("Generate Report"):
    
    # 1️⃣ Create some sample data
    data = {
        "Month": ["Jan", "Feb", "Mar", "Apr", "May"],
        "Sales": [1000, 1200, 900, 1500, 1300]
    }
    df = pd.DataFrame(data)
    
    # 2️⃣ Create an Excel file in memory
    output = BytesIO()
    with pd.ExcelWriter(output, engine="xlsxwriter") as writer:
        df.to_excel(writer, index=False, sheet_name="SalesData")
        
        # 3️⃣ Add a chart
        workbook  = writer.book
        worksheet = writer.sheets["SalesData"]
        
        chart = workbook.add_chart({"type": "line"})
        chart.add_series({
            "name":       "Sales",
            "categories": ["SalesData", 1, 0, 5, 0],  # Month column
            "values":     ["SalesData", 1, 1, 5, 1],  # Sales column
        })
        chart.set_title({"name": f"Monthly Sales for {customer}"})
        worksheet.insert_chart("D2", chart)
    
    # 4️⃣ Provide a download link
    output.seek(0)
    st.download_button(
        label="Download Excel Report",
        data=output,
        file_name=f"{customer}_sales_report.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
