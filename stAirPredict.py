import streamlit as st
import numpy as np
import joblib

model = joblib.load(r"C:\Users\sasam\Downloads\extra_trees_model.pkl")

st.title("🌍 Air Quality Prediction")

Temperature = st.number_input("Temperature")
Humidity = st.number_input("Humidity")
PM25 = st.number_input("PM2.5")
PM10 = st.number_input("PM10")
NO2 = st.number_input("NO2")
SO2 = st.number_input("SO2")
CO = st.number_input("CO")
Proximity = st.number_input("Proximity to Industrial Areas")
Population = st.number_input("Population Density")

if st.button("Predict"):

    input_data = np.array([[
        Temperature,
        Humidity,
        PM25,
        PM10,
        NO2,
        SO2,
        CO,
        Proximity,
        Population
    ]])

    prediction = model.predict(input_data)[0]

    labels = {
        0: "Good",
        1: "Moderate",
        2: "Poor",
        3: "Hazardous"
    }

    st.success(f"Predicted Air Quality: {labels[prediction]}")