import pandas as pd
import streamlit as st
from sklearn.datasets import load_wine
from sklearn.ensemble import (
    AdaBoostClassifier,
    GradientBoostingClassifier,
    RandomForestClassifier,
)
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from xgboost import XGBClassifier

st.set_page_config(
    page_title="Session 25: Wine Classifier Hub",
    page_icon="🍷",
    layout="wide",
)

st.title("🍷 Session 25: Wine Quality Classifier & Model Explorer")
st.write(
    "Explore models trained with manual tuning, Grid Search, and Boosting ensembles!"
)

# Load dataset and cache models
wine = load_wine()
X = pd.DataFrame(wine.data, columns=wine.feature_names)
y = wine.target


@st.cache_resource
def load_all_models():
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    trained_models = {
        "SVM (GridSearch Tuned)": SVC(C=1, kernel="linear").fit(X_scaled, y),
        "Random Forest": RandomForestClassifier(
            n_estimators=100, random_state=42
        ).fit(X_scaled, y),
        "AdaBoost": AdaBoostClassifier(n_estimators=100, random_state=42).fit(
            X_scaled, y
        ),
        "Gradient Boosting": GradientBoostingClassifier(
            n_estimators=100, learning_rate=0.1, random_state=42
        ).fit(X_scaled, y),
        "XGBoost": XGBClassifier(
            n_estimators=100, learning_rate=0.1, max_depth=3, random_state=42
        ).fit(X_scaled, y),
    }
    return trained_models, scaler, X.mean(axis=0)


models_dict, scaler, feature_means = load_all_models()

# Sidebar algorithm selector
selected_algo = st.sidebar.selectbox(
    "Choose Model Algorithm:", list(models_dict.keys())
)

st.subheader("Input Key Chemical Measurements:")
col1, col2, col3 = st.columns(3)

with col1:
    alcohol = st.number_input(
        "Alcohol", value=float(feature_means["alcohol"])
    )
    malic_acid = st.number_input(
        "Malic Acid", value=float(feature_means["malic_acid"])
    )
    ash = st.number_input("Ash", value=float(feature_means["ash"]))

with col2:
    alcalinity_of_ash = st.number_input(
        "Alcalinity of Ash", value=float(feature_means["alcalinity_of_ash"])
    )
    magnesium = st.number_input(
        "Magnesium", value=float(feature_means["magnesium"])
    )
    flavanoids = st.number_input(
        "Flavanoids", value=float(feature_means["flavanoids"])
    )

with col3:
    color_intensity = st.number_input(
        "Color Intensity", value=float(feature_means["color_intensity"])
    )
    hue = st.number_input("Hue", value=float(feature_means["hue"]))
    proline = st.number_input("Proline", value=float(feature_means["proline"]))

if st.button("Predict Wine Class", type="primary"):
    # Build complete feature array using mean defaults for unedited fields
    input_vector = feature_means.copy()
    input_vector["alcohol"] = alcohol
    input_vector["malic_acid"] = malic_acid
    input_vector["ash"] = ash
    input_vector["alcalinity_of_ash"] = alcalinity_of_ash
    input_vector["magnesium"] = magnesium
    input_vector["flavanoids"] = flavanoids
    input_vector["color_intensity"] = color_intensity
    input_vector["hue"] = hue
    input_vector["proline"] = proline

    input_df = pd.DataFrame([input_vector], columns=X.columns)
    scaled_input = scaler.transform(input_df)

    clf = models_dict[selected_algo]
    pred = clf.predict(scaled_input)[0]
    class_name = wine.target_names[pred]

    st.markdown("---")
    st.success(
        f"**Prediction ({selected_algo}):** 🍾 **Class {pred} ({class_name.upper()})**"
    )