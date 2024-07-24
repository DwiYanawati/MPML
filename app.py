import streamlit as st
import requests

# Input dari pengguna
family_size = st.number_input("Family Size", min_value=1)
gender = st.selectbox("Gender", ["Male", "Female"])
monthly_income = st.selectbox("Monthly Income", ["No Income", "Low", "Medium", "High"])

# Tombol untuk prediksi
if st.button("Predict"):
    # Kirim permintaan ke server backend
    url = "http://localhost:5000"
    data = {"family_size": family_size, "gender": gender, "monthly_income": monthly_income}
    response = requests.post(url, json=data)
    
    if response.status_code == 200:
        prediction = response.json().get("prediction")
        st.write(f"Prediction: {prediction}")
    else:
        st.write("Error:", response.status_code)
