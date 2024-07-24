import streamlit as st
import requests
import joblib
import pandas as pd

# Ganti dengan jalur absolut ke file model Anda
import os
import joblib

st.title('Customer Feedback Prediction App')

age = st.number_input('Age', min_value=0)
family_size = st.number_input('Family Size', min_value=1, max_value=10)
gender = st.selectbox('Gender', ['Male', 'Female'])
monthly_income = st.selectbox('Monthly Income', ['No Income', 'Below Rs.10000', '10001 to 25000', '25001 to 50000', 'More than 50000'])

if st.button('Predict'):
    data = {
        'Age': age,
        'Family_Size': family_size,
        'Gender': gender,
        'Monthly_Income': monthly_income
    }
    try:
        response = requests.post('http://localhost:5000/predict', json=data)
        result = response.json().get('prediction', 'Error: No prediction returned')
        st.write(f'Prediction: {result}')
    except Exception as e:
        st.write(f"Error: {str(e)}")
