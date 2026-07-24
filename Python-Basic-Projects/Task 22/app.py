# app.py
import joblib
import pandas as pd
import streamlit as st

# 1. Streamlit Page Configuration
st.set_page_config(
    page_title="Heart Disease Predictor", page_icon="❤️", layout="centered"
)

# 2. Title & Description
st.title("❤️ Heart Disease Prediction App")
st.write(
    "Fill in the patient's clinical metrics below to predict the likelihood of heart disease."
)
st.markdown("---")

# 3. Load Saved Model and Preprocessing Objects (columns.pkl)
try:
    model = joblib.load("heart_model.pkl")
    encoded_columns = joblib.load("columns.pkl")
    data_loaded = True
except FileNotFoundError:
    st.error(
        "❌ Missing required files! Please ensure 'heart_model.pkl' and 'columns.pkl' are in the same folder as this app."
    )
    data_loaded = False

if data_loaded:
    # 4. Streamlit Input Fields
    st.subheader("Patient Clinical Data")

    col1, col2 = st.columns(2)

    with col1:
        age = st.number_input(
            "Age (Years)", min_value=1, max_value=120, value=50, step=1
        )
        sex = st.selectbox(
            "Gender (Sex)", options=["M", "F"], help="M: Male, F: Female"
        )
        chest_pain = st.selectbox(
            "Chest Pain Type",
            options=["TA", "ATA", "NAP", "ASY"],
            help="TA: Typical Angina, ATA: Atypical Angina, NAP: Non-Anginal Pain, ASY: Asymptomatic",
        )
        resting_bp = st.number_input(
            "Resting Blood Pressure (mm Hg)",
            min_value=50,
            max_value=250,
            value=120,
            step=1,
        )
        cholesterol = st.number_input(
            "Serum Cholesterol (mm/dl)",
            min_value=0,
            max_value=700,
            value=200,
            step=1,
        )
        fasting_bs = st.selectbox(
            "Fasting Blood Sugar > 120 mg/dl",
            options=[0, 1],
            format_func=lambda x: "Yes (1)" if x == 1 else "No (0)",
        )

    with col2:
        resting_ecg = st.selectbox(
            "Resting ECG Results",
            options=["Normal", "ST", "LVH"],
            help="Normal: Normal, ST: ST-T wave abnormality, LVH: Left ventricular hypertrophy",
        )
        max_hr = st.number_input(
            "Maximum Heart Rate Achieved (MaxHR)",
            min_value=60,
            max_value=220,
            value=150,
            step=1,
        )
        exercise_angina = st.selectbox(
            "Exercise-Induced Angina",
            options=["N", "Y"],
            help="N: No, Y: Yes",
        )
        oldpeak = st.number_input(
            "Oldpeak (ST Depression)",
            min_value=-3.0,
            max_value=10.0,
            value=0.0,
            step=0.1,
        )
        st_slope = st.selectbox(
            "ST Slope",
            options=["Up", "Flat", "Down"],
            help="Slope of peak exercise ST segment",
        )

    st.markdown("---")

    # 5. On Button Click: Preprocess Input and Display Prediction
    predict_button = st.button("Predict Heart Disease", type="primary")

    if predict_button:
        try:
            # Step A: Collect input into a DataFrame
            input_df = pd.DataFrame(
                [
                    {
                        "Age": age,
                        "Sex": sex,
                        "ChestPainType": chest_pain,
                        "RestingBP": resting_bp,
                        "Cholesterol": cholesterol,
                        "FastingBS": fasting_bs,
                        "RestingECG": resting_ecg,
                        "MaxHR": max_hr,
                        "ExerciseAngina": exercise_angina,
                        "Oldpeak": oldpeak,
                        "ST_Slope": st_slope,
                    }
                ]
            )

            # Step B: Preprocess input (One-Hot Encoding)
            cat_cols = input_df.select_dtypes(include=["object"]).columns.tolist()
            input_encoded = pd.get_dummies(
                input_df, columns=cat_cols, drop_first=True
            ).astype(int)

            # Align with columns saved in columns.pkl
            input_aligned = input_encoded.reindex(
                columns=encoded_columns, fill_value=0
            )

            # Step C: Make Prediction using loaded model
            prediction = model.predict(input_aligned)[0]

            # Step D: Display Prediction Result using st.error() or st.success()
            st.markdown("### Diagnosis Result")
            if prediction == 1:
                st.error("🚨 **Heart Disease: Yes**")
            else:
                st.success("✅ **Heart Disease: No**")

        except Exception as e:
            st.error(f"An error occurred while making predictions: {e}")