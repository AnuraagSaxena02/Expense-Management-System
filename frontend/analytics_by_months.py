import streamlit as st
import requests
import pandas as pd

API_URL = "http://localhost:8000"

def analytics_months_tab():
    response = requests.get(f"{API_URL}/monthly_summary/")
    monthly_summary = response.json()

    if not monthly_summary:
        st.warning("No data available")
        return

    if isinstance(monthly_summary, dict):
        monthly_summary = [monthly_summary]

    df = pd.DataFrame(monthly_summary)

    st.write("Columns:", df.columns.tolist())
    st.write("Data:", df)

    if "expense_month" in df.columns:
        df = df.rename(columns={
            "expense_month": "Month Number",
            "month_name": "Month Name",
            "total": "Total"
        })

        df_sorted = df.sort_values(by="Month Number", ascending=True)

        st.title("Expense Breakdown By Months")

        st.bar_chart(
            data=df_sorted.set_index("Month Name")['Total'],
            width='stretch'
        )

        df_sorted["Total"] = df_sorted["Total"].map("{:.2f}".format)

        st.table(df_sorted)
    else:
        st.error("Unexpected API response")