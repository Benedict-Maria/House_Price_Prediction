import streamlit as st
import pandas as pd
import joblib

model = joblib.load("house_price_prediction_model.joblib")

st.title("House Price Prediction Web App")

st.write("Enter the house details to get the predicted price:")

area = st.number_input("Area (sq ft)", min_value=500, max_value=10000, value=2000)
bedrooms = st.number_input("Bedrooms", min_value=1, max_value=10, value=3)
bathrooms = st.number_input("Bathrooms", min_value=1, max_value=5, value=2)
stories = st.number_input("Stories", min_value=1, max_value=5, value=2)
parking = st.number_input("Parking (0–5)", min_value=0, max_value=5, value=1)

mainroad = st.selectbox("Mainroad", ["yes", "no"])
guestroom = st.selectbox("Guestroom", ["yes", "no"])
basement = st.selectbox("Basement", ["yes", "no"])
hotwaterheating = st.selectbox("Hotwater Heating", ["yes", "no"])
airconditioning = st.selectbox("Airconditioning", ["yes", "no"])
prefarea = st.selectbox("Preferred Area", ["yes", "no"])
furnishingstatus = st.selectbox("Furnishing Status",
                                ["furnished", "semi-furnished", "unfurnished"])

if st.button("Predict Price"):
    new_data = pd.DataFrame([{
        "area": area,
        "bedrooms": bedrooms,
        "bathrooms": bathrooms,
        "stories": stories,
        "parking": parking,
        "mainroad": mainroad,
        "guestroom": guestroom,
        "basement": basement,
        "hotwaterheating": hotwaterheating,
        "airconditioning": airconditioning,
        "prefarea": prefarea,
        "furnishingstatus": furnishingstatus
    }])

    pred = model.predict(new_data)[0]
    st.success(f"Predicted Price: ${pred:,.0f}")
