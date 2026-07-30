import numpy as np
import pandas as pd
import streamlit as st
from sklearn.datasets import fetch_california_housing, load_breast_cancer
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import StandardScaler

st.set_page_config(page_title="Task 23 ML Models", layout="wide")
st.title("🤖 Session 23: Machine Learning Model Explorer")

# Sidebar navigation
app_mode = st.sidebar.selectbox(
    "Choose a Task / Model:",
    [
        "Q1: Linear Regression (Housing)",
        "Q2-Q5: Classification Models (Cancer Dataset)",
    ],
)


# TAB 1: Linear Regression


if app_mode == "Q1: Linear Regression (Housing)":
    st.header("🏠 Q1: California House Price Prediction")

    # Load & Train
    housing = fetch_california_housing(as_frame=True)
    X_train, X_test, y_train, y_test = train_test_split(
        housing.data, housing.target, test_size=0.2, random_state=42
    )
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)

    model = LinearRegression()
    model.fit(X_train_scaled, y_train)

    st.write("Enter values below to estimate house value:")
    med_inc = st.number_input("Median Income ($10k)", value=3.5)
    house_age = st.number_input("House Age", value=25.0)
    ave_rooms = st.number_input("Average Rooms", value=5.0)
    ave_occup = st.number_input("Average Occupants", value=3.0)

    if st.button("Predict House Value"):
        # Construct input with default median values for remaining features
        input_data = np.array(
            [[med_inc, house_age, ave_rooms, 1.0, ave_occup, 2.5, 37.8, -122.2]]
        )
        input_scaled = scaler.transform(input_data)
        prediction = model.predict(input_scaled)[0]
        st.success(f"Predicted Value: **${prediction * 100000:,.2f}**")



# TAB 2: Classification Models

else:
    st.header("🔬 Binary Classification Task Explorer")

    # Select Algorithm
    algo = st.selectbox(
        "Select Model Algorithm:",
        ["Logistic Regression", "KNN Classifier", "Naive Bayes"],
    )

    k_val = 5
    if algo == "KNN Classifier":
        k_val = st.slider("Select k (Number of Neighbors):", 1, 15, 5, step=2)

    # Load & Train
    cancer = load_breast_cancer()
    X_train, X_test, y_train, y_test = train_test_split(
        cancer.data, cancer.target, test_size=0.2, random_state=42
    )

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)

    if algo == "Logistic Regression":
        clf = LogisticRegression(random_state=42)
    elif algo == "KNN Classifier":
        clf = KNeighborsClassifier(n_neighbors=k_val)
    else:
        clf = GaussianNB()

    clf.fit(X_train_scaled, y_train)

    st.subheader("Interactive Prediction Test")
    col1, col2 = st.columns(2)
    with col1:
        mean_radius = st.number_input("Mean Radius", value=14.0)
        mean_texture = st.number_input("Mean Texture", value=19.0)
    with col2:
        mean_perimeter = st.number_input("Mean Perimeter", value=90.0)
        mean_area = st.number_input("Mean Area", value=650.0)

    if st.button("Classify Tumor Risk"):
        # Dummy full vector filled with training averages
        sample = X_train.mean(axis=0)
        sample[0] = mean_radius
        sample[1] = mean_texture
        sample[2] = mean_perimeter
        sample[3] = mean_area

        sample_scaled = scaler.transform([sample])
        pred = clf.predict(sample_scaled)[0]
        label = cancer.target_names[pred]

        if label == "benign":
            st.success(f"Prediction: **{label.upper()}** (Low Risk)")
        else:
            st.error(f"Prediction: **{label.upper()}** (High Risk)")