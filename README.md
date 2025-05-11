# Healthcare Cost Prediction

This project predicts healthcare insurance charges based on various factors using machine learning.

## Features
- Age
- Sex
- BMI
- Number of Children
- Smoking Status
- Region

## Technologies Used
- Python
- Scikit-learn
- Streamlit
- Pandas
- NumPy

## Setup and Installation
1. Clone the repository
2. Install required packages:
   ```
   pip install -r requirements.txt
   ```
3. Run the Streamlit app:
   ```
   streamlit run webapp.py
   ```

## Model Performance
- R² Score: 0.784
- RMSE: $5,796.28

## Project Structure
- `webapp.py`: Streamlit web application
- `insurance_model.pkl`: Trained machine learning model
- `insurance_preprocessor.pkl`: Data preprocessor
- `healthdata.csv`: Dataset used for training 