import streamlit as st
import pandas as pd

st.title("Expense Management System")

expense_dt = st.date_input("Expense Date:")
Age = st.number_input("Enter your age:")
Name = st.text_input("Enter your name:")
if expense_dt:
    st.write(f"Fetching expenses for {expense_dt}")

#Text elements
st.header("Streamlit Core Features")
st.subheader("Text Elements")
st.text("This is simple text elements")

#Data display
st.subheader("Data Display")
st.write("Here is a simple table:")
st.table({"Column 1":[1,2,3],'column 2':[4,5,6],'column 3':[7,8,9]})

#Charts
st.subheader("Charts")
st.line_chart([1,2,3,4])

df = pd.DataFrame({
    'Date':["2024-08-01","2024-08-02","2024-08-03","2024-08-04"],
    'Amount':[10,20,30,40]
})
st.table(df)

#User Input
st.subheader("User Input")
value = st.slider("Select your value", min_value=0, max_value=10, value=0)
st.write(f"Selected value: {value}")

#Checkbox
if st.checkbox("Show/Hide"):
   st.write("Checkbox is checked")

#Selectbox
option = st.selectbox("Select a number",[1,2,3,4])
st.write(f"Selected option: {option}")

option = st.selectbox("Category",["Rent","Food"],label_visibility="collapsed")
st.write(f"Selected option: {option}")

#Multiselect
options = st.multiselect("Select multiple numbers", [1,2,3,4])
st.write(f"Selected option: {options}")