import streamlit as st

import pandas as pd

import numpy as np

import joblib
 
# Load the trained model and preprocessor

model = joblib.load('insurance_model.pkl')

preprocessor = joblib.load('insurance_preprocessor.pkl')
 
st.title("Heathcare Charges Predictor")
 
st.write("Enter the details below to predict medical expenses:")
 
# User input widgets

age = st.number_input("Age", min_value=18, max_value=100, value=30)

sex = st.selectbox("Sex", options=['male', 'female'])

bmi = st.number_input("BMI", min_value=10.0, max_value=60.0, value=25.0, step=0.1)

children = st.number_input("Number of Children", min_value=0, max_value=5, value=0)

smoker = st.selectbox("Smoker", options=['yes', 'no'])

region = st.selectbox("Region", options=['northeast', 'northwest', 'southeast', 'southwest'])
 
if st.button("Predict Charges"):
    # Calculate derived features
    age_squared = age ** 2
    bmi_squared = bmi ** 2
    age_bmi = age * bmi
    smoker_bmi = 1 * bmi if smoker == 'yes' else 0 * bmi
    
    # Prepare input data as a DataFrame
    input_df = pd.DataFrame({
        'age': [age],
        'sex': [sex],
        'bmi': [bmi],
        'children': [children],
        'smoker': [smoker],
        'region': [region],
        'age_squared': [age_squared],
        'bmi_squared': [bmi_squared],
        'age_bmi': [age_bmi],
        'smoker_bmi': [smoker_bmi]
    })
 
    # Preprocess input
    input_processed = preprocessor.transform(input_df)
 
    # Predict
    prediction = model.predict(input_processed)[0]
 
    st.success(f"Predicted Insurance Charges: ${prediction:,.2f}")

 