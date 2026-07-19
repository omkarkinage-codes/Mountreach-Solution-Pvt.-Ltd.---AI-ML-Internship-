# app.py

# Q1. Setup and Libraries

# streamlit: Used to build the interactive web application interface and handle layout elements.
import streamlit as st

# pandas: Used for data manipulation, structure handling (DataFrames), and preprocessing inputs.
import pandas as pd

# joblib: Used to deserialize and load the pre-trained machine learning model, scaler, and column list.
import joblib


# Q3. Page Configuration

# Configures the browser tab title and forces a clean, centered interface layout.
st.set_page_config(page_title="Ford Car Price Predictor", layout="centered")


# Q2. Loading Model and Preprocessing Objects

# Using try-except block for Q10 error handling requirement
try:
    model = joblib.load("LR_ford_car.pkl")
    scaler = joblib.load("scaler.pkl")
    encoded_columns = joblib.load("columns.pkl")
    data_loaded_successfully = True
except FileNotFoundError as e:
    st.error(
        f"Initialization Error: Could not find required model file. Ensure you are running the app from the correct directory containing your .pkl files."
    )
    data_loaded_successfully = False

# Only render the rest of the application interface if the files loaded successfully
if data_loaded_successfully:

    # Q4. Title and Description

    st.title("🚗 Ford Car Price Predictor")
    st.write("Enter the car details below to predict its estimated selling price.")
    st.markdown("---")


    # Q7. Text Input (Car Model Name)

    st.subheader("Car Specifications")
    model_name = st.text_input(
        "Car Model Name", placeholder="e.g., Focus, Fiesta, Mustang, EcoSport"
    )

    # Organizing fields using columns for a cleaner, responsive grid layout
    col1, col2 = st.columns(2)

    with col1:

        # Q5. Numerical Input Fields (Part 1)

        year = st.number_input(
            "Manufacturing Year", min_value=2000, max_value=2026, value=2018, step=1
        )
        mileage = st.number_input(
            "Total Mileage", min_value=0, max_value=400000, value=30000, step=1000
        )
        tax = st.number_input(
            "Road Tax (£)", min_value=0, max_value=1000, value=145, step=5
        )

    with col2:

        # Q5. Numerical Input Fields (Part 2)

        mpg = st.number_input(
            "Miles Per Gallon (MPG)",
            min_value=10.0,
            max_value=120.0,
            value=55.4,
            step=0.1,
        )
        engineSize = st.number_input(
            "Engine Size (Liters)", min_value=0.0, max_value=8.0, value=1.5, step=0.1
        )


        # Q6. Categorical Input Dropdowns

        transmission = st.selectbox(
            "Transmission Type", options=["Manual", "Automatic", "Semi-Auto"]
        )

    fuel_type = st.selectbox(
        "Fuel Type", options=["Petrol", "Diesel", "Hybrid", "Electric", "Other"]
    )

    st.markdown("---")


    # Q7. Predict Button

    predict_button = st.button("Predict Selling Price", type="primary")

    if predict_button:
        # Validation handling to make sure user typed a model name
        if not model_name.strip():
            st.warning("Please enter a valid Car Model Name before predicting.")
        else:
            try:

                # Q8. Creating Input DataFrame & Encoding

                input_data = pd.DataFrame(
                    [
                        {
                            "Year": year,
                            "Engine Size": engineSize,
                            "Mileage": mileage,
                            "Fuel Type": fuel_type,
                            "Transmission": transmission,
                            "Model": model_name.strip(),
                            "Make": "Ford",
                        }
                    ]
                )

                # Generate dummies for the categorical inputs
                input_encoded = pd.get_dummies(input_data)

                # Reindex structure to match training columns perfectly
                input_aligned = input_encoded.reindex(
                    columns=encoded_columns, fill_value=0
                )

                # Q9. Feature Scaling and Prediction

                numeric_features = ["Year", "Mileage", "Engine Size"]
                input_aligned[numeric_features] = scaler.transform(
                    input_aligned[numeric_features]
                )

                # Execute mathematical model prediction
                prediction = model.predict(input_aligned)[0]

                # Ensure predicted values do not fall realistically below zero
                if prediction < 0:
                    prediction = 0.0

                # Render final prediction box to the user interface
                st.success(f"### Estimated Value: £{prediction:,.2f}")

            except Exception as prediction_error:
                st.error(
                    f"An error occurred during data processing: {prediction_error}"
                )