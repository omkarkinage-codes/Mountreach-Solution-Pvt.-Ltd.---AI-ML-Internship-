# app_diabetes.py
import os
import joblib
import pandas as pd
import streamlit as st

# 1. Page Configuration
st.set_page_config(page_title="Diabetes Risk Predictor", page_icon="🩸")

st.title("🩸 Diabetes Risk Prediction App")
st.write("Enter patient metrics below to evaluate diabetes risk.")
st.markdown("---")

# 2. Get current script directory to construct absolute file paths safely
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model_path = os.path.join(BASE_DIR, "diabetes_model.pkl")
scaler_path = os.path.join(BASE_DIR, "diabetes_scaler.pkl")
columns_path = os.path.join(BASE_DIR, "diabetes_columns.pkl")

# Load Model Artifacts
try:
    model = joblib.load(model_path)
    scaler = joblib.load(scaler_path)
    columns = joblib.load(columns_path)
    loaded = True
except FileNotFoundError:
    st.error("❌ Model files not found! Please ensure .pkl files exist in the app directory.")
    loaded = False

if loaded:
    # 3. Input Layout
    col1, col2 = st.columns(2)

    with col1:
        pregnancies = st.number_input(
            "Pregnancies", min_value=0, max_value=20, value=1, step=1
        )
        glucose = st.number_input(
            "Glucose Level", min_value=40.0, max_value=300.0, value=120.0
        )
        blood_pressure = st.number_input(
            "Blood Pressure (mm Hg)",
            min_value=30.0,
            max_value=180.0,
            value=70.0,
        )
        skin_thickness = st.number_input(
            "Skin Thickness (mm)", min_value=5.0, max_value=100.0, value=20.0
        )

    with col2:
        insulin = st.number_input(
            "Insulin Level", min_value=5.0, max_value=900.0, value=80.0
        )
        bmi = st.number_input(
            "BMI", min_value=10.0, max_value=70.0, value=25.0
        )
        dpf = st.number_input(
            "Diabetes Pedigree Function",
            min_value=0.01,
            max_value=3.0,
            value=0.47,
            step=0.01,
        )
        age = st.number_input("Age", min_value=10, max_value=120, value=30)

    st.markdown("---")

    # 4. Predict Button
    if st.button("Predict Diabetes Risk", type="primary"):
        input_data = pd.DataFrame(
            [
                {
                    "Pregnancies": pregnancies,
                    "Glucose": glucose,
                    "BloodPressure": blood_pressure,
                    "SkinThickness": skin_thickness,
                    "Insulin": insulin,
                    "BMI": bmi,
                    "DiabetesPedigreeFunction": dpf,
                    "Age": age,
                }
            ]
        )

        # Enforce exact column order from training time
        input_data = input_data[columns]

        # Scale inputs and predict
        input_scaled = scaler.transform(input_data)
        prediction = model.predict(input_scaled)[0]
        prob = model.predict_proba(input_scaled)[0]

        # 5. Display Result
        st.subheader("Result:")
        if prediction == 1:
            st.error(
                f"🚨 **High Risk: Diabetes Detected** (Confidence: {prob[1] * 100:.2f}%)"
            )
        else:
            st.success(
                f"✅ **Low Risk: No Diabetes Detected** (Confidence: {prob[0] * 100:.2f}%)"
            )
