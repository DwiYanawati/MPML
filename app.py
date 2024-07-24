import streamlit as st
import joblib
import pandas as pd
import os

# Tentukan jalur absolut untuk file model
model_path = os.path.join('/mount/src/MPML', 'best_model.pkl')
print(f"Attempting to load model from: {model_path}")

if not os.path.isfile(model_path):
    raise FileNotFoundError(f"Model file {model_path} does not exist.")
else:
    print(f"File {model_path} found.")

model = joblib.load(model_path)

# Daftar fitur yang diharapkan oleh model
expected_features = [
    'Gender', 'Marital Status', 'Occupation', 'Monthly Income', 
    'Educational Qualifications', 'Age', 'Family size', 'latitude', 
    'longitude', 'Pin code'
]

# Streamlit application
def main():
    st.title('Welcome to the Customer Feedback Prediction App')

    # Form for input
    with st.form(key='prediction_form'):
        gender = st.selectbox('Gender', ['Male', 'Female'])
        marital_status = st.selectbox('Marital Status', ['Single', 'Married', 'Prefer Not to Say'])
        occupation = st.selectbox('Occupation', ['Employee', 'Student', 'Self Employed', 'House Wife', 'Other'])
        monthly_income = st.selectbox('Monthly Income', ['No Income', 'Below Rs.10000', '10001 to 25000', '25001 to 50000', 'More than 50000'])
        educational_qualifications = st.selectbox('Educational Qualifications', ['Graduate', 'Post Graduate', 'Ph.D', 'School', 'Uneducated'])
        age = st.number_input('Age', min_value=0)
        family_size = st.number_input('Family Size', min_value=1, max_value=10)
        latitude = st.number_input('Latitude')
        longitude = st.number_input('Longitude')
        pin_code = st.number_input('Pin Code')

        submit_button = st.form_submit_button(label='Predict')

        if submit_button:
            # Create DataFrame for prediction
            data = pd.DataFrame({
                'Gender': [gender],
                'Marital Status': [marital_status],
                'Occupation': [occupation],
                'Monthly Income': [monthly_income],
                'Educational Qualifications': [educational_qualifications],
                'Age': [age],
                'Family size': [family_size],
                'latitude': [latitude],
                'longitude': [longitude],
                'Pin code': [pin_code]
            })

            # Validasi fitur
            if list(data.columns) != expected_features:
                st.error("Fitur yang diberikan tidak sesuai dengan yang diharapkan oleh model.")
            else:
                # Predict
                prediction = model.predict(data)[0]
                st.write(f'Prediction: {prediction}')

if __name__ == "__main__":
    main()
