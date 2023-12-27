import streamlit as st
import pandas as pd
import pickle

# Load the trained model

model = pickle.load(open('LinearRegressionModel.pkl', 'rb'))

# Function to get unique sorted values from a column in the dataset
car = pd.read_csv("Cleaned data.csv")

st.title("Welcome to Car Price Predictor")

# Initial values for input fields
selected_company = ''
selected_model = ''
selected_year = ''
selected_fuel_type = ''
kilometers_driven = 0

selected_company = st.selectbox("Select the company", [''] + sorted(car['company'].unique()))

# Prepopulate models based on the first company in the list
selected_models_options = []
if selected_company:
    selected_models_options = sorted(car[car['company'] == selected_company]['name'].unique())

selected_model = st.selectbox("Select the model", [''] + selected_models_options)

selected_year = st.selectbox("Select the year of purchase", [''] + sorted(car['year'].unique(), reverse=True))
selected_fuel_type = st.selectbox("Select the fuel type", [''] + sorted(car['fuel_type'].unique()))
kilometers_driven = st.number_input("Enter the number of kilometers driven", value=kilometers_driven)

predict_button = st.button("Predict Price")

if predict_button and selected_company and selected_model and selected_year and selected_fuel_type:
    # Prepare data for prediction
    input_data = pd.DataFrame({
        'name': [selected_model],
        'company': [selected_company],
        'year': [selected_year],
        'kms_driven': [kilometers_driven],
        'fuel_type': [selected_fuel_type]
    })

    # Match column names with the columns used during model training
    input_data = input_data[['name', 'company', 'year', 'kms_driven', 'fuel_type']]

    # Predict the price using the model
    predicted_price = model.predict(input_data)[0]

    st.success(f"The predicted price of the car is: {predicted_price:.2f} INR")