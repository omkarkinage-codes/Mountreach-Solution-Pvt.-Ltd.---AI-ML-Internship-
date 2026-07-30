import numpy as np
import pandas as pd
import streamlit as st
from sklearn.datasets import fetch_california_housing, fetch_openml
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.neighbors import KNeighborsClassifier, KNeighborsRegressor
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC, SVR
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor


# Page Configuration

st.set_page_config(
    page_title="Session 24: Multi-Model ML Hub",
    page_icon="⚡",
    layout="wide",
)

st.title("⚡ Multi-Model ML Hub (Session 24)")
st.write(
    "Select a problem type, pick an algorithm, enter feature values, and see live predictions!"
)


# Sidebar Navigation

problem_type = st.sidebar.radio(
    "1. Select Problem Type:", ["Classification", "Regression"]
)


# PROBLEM TYPE 1: CLASSIFICATION (Diabetes Prediction)

if problem_type == "Classification":
    st.header("🩸 Diabetes Risk Classification")

    algo_choice = st.sidebar.selectbox(
        "2. Choose Classification Algorithm:",
        [
            "Logistic Regression",
            "Decision Tree Classifier",
            "Support Vector Machine (SVM)",
            "K-Nearest Neighbors (KNN)",
            "Naive Bayes",
        ],
    )

    # Load Classification Dataset & Train Models dynamically
    @st.cache_resource
    def load_clf_data_and_models():
        diabetes = fetch_openml(name="diabetes", version=1, as_frame=True)
        X = diabetes.data
        y = (diabetes.target == "tested_positive").astype(int)

        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)

        models = {
            "Logistic Regression": LogisticRegression(random_state=42).fit(
                X_scaled, y
            ),
            "Decision Tree Classifier": DecisionTreeClassifier(
                random_state=42
            ).fit(X, y),
            "Support Vector Machine (SVM)": SVC(
                probability=True, random_state=42
            ).fit(X_scaled, y),
            "K-Nearest Neighbors (KNN)": KNeighborsClassifier(
                n_neighbors=5
            ).fit(X_scaled, y),
            "Naive Bayes": GaussianNB().fit(X_scaled, y),
        }
        return models, scaler, X, X.mean(axis=0)

    models_dict, scaler_clf, X_clf_df, clf_means = load_clf_data_and_models()

    st.subheader("Input Patient Parameters:")
    col1, col2 = st.columns(2)

    with col1:
        preg = st.number_input(
            "Pregnancies",
            min_value=0,
            max_value=20,
            value=int(clf_means["preg"]),
        )
        plas = st.number_input(
            "Glucose Level (plas)",
            min_value=0.0,
            max_value=300.0,
            value=float(clf_means["plas"]),
        )
        pres = st.number_input(
            "Blood Pressure (pres)",
            min_value=0.0,
            max_value=200.0,
            value=float(clf_means["pres"]),
        )
        skin = st.number_input(
            "Skin Thickness (skin)",
            min_value=0.0,
            max_value=100.0,
            value=float(clf_means["skin"]),
        )

    with col2:
        insu = st.number_input(
            "Insulin Level (insu)",
            min_value=0.0,
            max_value=900.0,
            value=float(clf_means["insu"]),
        )
        mass = st.number_input(
            "BMI (mass)",
            min_value=0.0,
            max_value=70.0,
            value=float(clf_means["mass"]),
        )
        pedi = st.number_input(
            "Diabetes Pedigree Function (pedi)",
            min_value=0.0,
            max_value=3.0,
            value=float(clf_means["pedi"]),
            step=0.01,
        )
        age = st.number_input(
            "Age", min_value=1, max_value=120, value=int(clf_means["age"])
        )

    if st.button("Predict Diabetes Risk", type="primary"):
        input_data = pd.DataFrame(
            [
                [preg, plas, pres, skin, insu, mass, pedi, age]
            ],
            columns=X_clf_df.columns,
        )

        selected_model = models_dict[algo_choice]

        if algo_choice == "Decision Tree Classifier":
            pred = selected_model.predict(input_data)[0]
        else:
            scaled_input = scaler_clf.transform(input_data)
            pred = selected_model.predict(scaled_input)[0]

        st.markdown("---")
        if pred == 1:
            st.error(
                f"**Prediction Result ({algo_choice}):** 🚨 **DIABETIC (High Risk)**"
            )
        else:
            st.success(
                f"**Prediction Result ({algo_choice}):** ✅ **NON-DIABETIC (Low Risk)**"
            )


# PROBLEM TYPE 2: REGRESSION (Housing Price Prediction)

else:
    st.header("🏠 California House Price Prediction")

    algo_choice = st.sidebar.selectbox(
        "2. Choose Regression Algorithm:",
        [
            "Linear Regression",
            "Decision Tree Regressor",
            "Support Vector Regressor (SVR)",
            "K-Nearest Neighbors Regressor",
        ],
    )

    @st.cache_resource
    def load_reg_data_and_models():
        housing = fetch_california_housing(as_frame=True)
        X = housing.data
        y = housing.target

        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)

        models = {
            "Linear Regression": LinearRegression().fit(X_scaled, y),
            "Decision Tree Regressor": DecisionTreeRegressor(
                random_state=42
            ).fit(X, y),
            "Support Vector Regressor (SVR)": SVR().fit(X_scaled, y),
            "K-Nearest Neighbors Regressor": KNeighborsRegressor(
                n_neighbors=5
            ).fit(X_scaled, y),
        }
        return models, scaler, X, X.mean(axis=0)

    reg_models_dict, scaler_reg, X_reg_df, reg_means = load_reg_data_and_models()

    st.subheader("Input House Metrics:")
    col1, col2 = st.columns(2)

    with col1:
        med_inc = st.number_input(
            "Median Income ($10,000s)", value=float(reg_means["MedInc"])
        )
        house_age = st.number_input(
            "House Age", value=float(reg_means["HouseAge"])
        )
        ave_rooms = st.number_input(
            "Average Rooms", value=float(reg_means["AveRooms"])
        )
        ave_bedrms = st.number_input(
            "Average Bedrooms", value=float(reg_means["AveBedrms"])
        )

    with col2:
        population = st.number_input(
            "Population", value=float(reg_means["Population"])
        )
        ave_occup = st.number_input(
            "Average Occupants", value=float(reg_means["AveOccup"])
        )
        latitude = st.number_input(
            "Latitude", value=float(reg_means["Latitude"])
        )
        longitude = st.number_input(
            "Longitude", value=float(reg_means["Longitude"])
        )

    if st.button("Estimate House Price", type="primary"):
        input_data = pd.DataFrame(
            [
                [
                    med_inc,
                    house_age,
                    ave_rooms,
                    ave_bedrms,
                    population,
                    ave_occup,
                    latitude,
                    longitude,
                ]
            ],
            columns=X_reg_df.columns,
        )

        selected_model = reg_models_dict[algo_choice]

        if algo_choice == "Decision Tree Regressor":
            pred_val = selected_model.predict(input_data)[0]
        else:
            scaled_input = scaler_reg.transform(input_data)
            pred_val = selected_model.predict(scaled_input)[0]

        st.markdown("---")
        st.success(
            f"**Estimated Price ({algo_choice}):** **${pred_val * 100000:,.2f}**"
        )