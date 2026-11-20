import streamlit as st
import pickle
import pandas as pd

st.set_page_config(page_title="House Price Prediction", page_icon="🏠")

with open("house_price_model.pkl", "rb") as file:
    model = pickle.load(file)

st.title("🏠 House Price Prediction")
st.write("Machine Learning using Linear Regression")
st.divider()
st.subheader("Enter House Details")

area = st.number_input("Enter Area (sq ft)", min_value=100, max_value=10000, value=1200)
bedrooms = st.number_input("Enter Bedrooms", min_value=1, max_value=10, value=3)
bathrooms = st.number_input("Enter Bathrooms", min_value=1, max_value=10, value=2)

if st.button("Predict House Price"):
    input_data = pd.DataFrame(
        [[area, bedrooms, bathrooms]],
        columns=["area", "bedrooms", "bathrooms"]
    )
    price = model.predict(input_data)[0]
    st.success("Prediction Successful!")
    st.subheader("Estimated House Price")
    st.write("₹", round(price, 2), "Lakh")
    st.write("Area:", area, "sq ft")
    st.write("Bedrooms:", bedrooms)
    st.write("Bathrooms:", bathrooms)

st.divider()
st.subheader("About Project")
st.write("This project predicts house prices using Linear Regression.")
