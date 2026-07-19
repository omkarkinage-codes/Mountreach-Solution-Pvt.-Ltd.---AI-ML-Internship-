# app_rf.py
import joblib
import pandas as pd
import streamlit as st

# 1. Page Configuration
st.set_page_config(page_title="Multi-Brand Car Price Predictor", layout="centered")

# 2. Load Pretrained Objects
try:
    model = joblib.load("LR_ford_car.pkl")
    scaler = joblib.load("scaler.pkl")
    encoded_columns = joblib.load("columns.pkl")
    data_loaded_successfully = True
except FileNotFoundError:
    st.error(
        "❌ Missing model files! Make sure 'LR_ford_car.pkl', 'scaler.pkl', and 'columns.pkl' are in the same folder as this script."
    )
    data_loaded_successfully = False

if data_loaded_successfully:
    # 3. Title and Description
    st.title("🚗 Universal Car Price Predictor")
    st.write(
        "Enter the manufacturer specifications below to evaluate the estimated vehicle market value."
    )
    st.markdown("---")

    # 4. Input Fields
    st.subheader("Vehicle Specifications")

    make = st.selectbox(
        "Manufacturer (Make)", options=["BMW", "Ford", "Honda", "Toyota"]
    )
    model_name = st.selectbox(
        "Vehicle Model", options=["Model B", "Model C", "Model D", "Model E"]
    )

    col1, col2 = st.columns(2)

    with col1:
        year = st.number_input(
            "Manufacturing Year", min_value=2000, max_value=2026, value=2018, step=1
        )
        mileage = st.number_input(
            "Odometer Mileage", min_value=0, max_value=400000, value=35000, step=1000
        )

    with col2:
        engineSize = st.number_input(
            "Engine Size (Liters)", min_value=0.5, max_value=8.0, value=2.0, step=0.1
        )
        transmission = st.selectbox(
            "Transmission Type", options=["Manual", "Automatic"]
        )

    fuel_type = st.selectbox(
        "Fuel Profile", options=["Petrol", "Diesel", "Electric", "Hybrid"]
    )

    st.markdown("---")

    # 5. Predict Button Trigger
    predict_button = st.button("Generate Random Forest Valuation", type="primary")

    if predict_button:
        try:
            # 1. Create base DataFrame following original layout structure
            input_data = pd.DataFrame(
                [
                    {
                        "Year": year,
                        "Engine Size": engineSize,
                        "Mileage": mileage,
                        "Make": make,
                        "Model": model_name,
                        "Fuel Type": fuel_type,
                        "Transmission": transmission,
                    }
                ]
            )

            # 2. Apply One-Hot Encoding targeting categorical elements
            input_encoded = pd.get_dummies(
                input_data,
                columns=["Make", "Model", "Fuel Type", "Transmission"],
                drop_first=True,
            ).astype(int)

            # 3. Align the structural dummy columns with training format
            input_aligned = input_encoded.reindex(
                columns=encoded_columns, fill_value=0
            )

            # 4. Extract numerical features and apply scaler
            numeric_features = ["Year", "Mileage", "Engine Size"]
            input_aligned[numeric_features] = scaler.transform(
                input_aligned[numeric_features]
            )

            # 5. Make prediction using your Random Forest model
            prediction = model.predict(input_aligned)[0]

            st.success(f"### Estimated Value Output: ${prediction:,.2f}")

        except Exception as e:
            st.error(f"An error occurred during computational processing: {e}")