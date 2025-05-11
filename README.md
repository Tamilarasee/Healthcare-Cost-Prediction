# Healthcare Charges Predictor

This project predicts healthcare expenses (medical charges) billed to insurance based on personal information using linear regression with enhanced feature engineering.

## Overview

The Healthcare Charges Predictor uses machine learning to estimate medical expenses based on demographic and health-related inputs. The model is built using a linear regression algorithm with advanced feature engineering to improve prediction accuracy.

## Try It Out

The application is deployed and available to use online: [Healthcare Charges Predictor App](https://heathcare-cost-prediction.streamlit.app/)

## Files

- `Final_project.ipynb`: Jupyter notebook containing the data analysis, model training, and evaluation 
- `webapp.py`: Streamlit web application that provides a user interface for the prediction model
- `insurance_model.pkl`: Saved machine learning model
- `insurance_preprocessor.pkl`: Saved data preprocessing pipeline
- `healthdata.csv`: Dataset used for training the model

## Features

The prediction model uses the following input features:
- Age
- Sex (male/female)
- BMI (Body Mass Index)
- Number of children
- Smoker status (yes/no)
- Region (northeast, northwest, southeast, southwest)

## Enhanced Feature Engineering

To improve model performance, the following derived features are calculated:
- `age_squared`: Captures non-linear relationship between age and healthcare charges
- `bmi_squared`: Captures non-linear relationship between BMI and healthcare charges
- `age_bmi`: Interaction between age and BMI factors
- `smoker_bmi`: Interaction between smoking status and BMI

## Web Application

The Streamlit web application provides an intuitive interface for users to input their information and receive a prediction of their potential healthcare charges. The app automatically calculates derived features to enhance prediction accuracy.

## Running the Application Locally

1. Ensure you have Python installed along with the required packages:
   ```
   pip install streamlit pandas numpy scikit-learn joblib
   ```

2. Run the Streamlit application:
   ```
   streamlit run webapp.py
   ```

3. Enter your information in the form and click "Predict Charges" to get your estimated healthcare expenses.

## Model Performance

The linear regression model with enhanced feature engineering achieves strong performance:
- R² Score: Measures how well the model explains the variation in healthcare charges
- RMSE: Measures the average prediction error in dollar amount

## Future Improvements

Potential future enhancements include:
- Adding more health-related features
- Incorporating regional cost-of-living adjustments
- Developing personalized recommendations for reducing healthcare expenses

---

This project demonstrates the power of effective feature engineering in improving linear regression models without requiring more complex machine learning algorithms. 