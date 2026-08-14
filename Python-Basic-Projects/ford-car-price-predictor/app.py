import joblib
import pandas as pd
import streamlit as st

# ------------------------------------------------------------
# PAGE
# ------------------------------------------------------------
st.set_page_config(
    page_title="Ford Car Price Predictor",
    page_icon="🚗",
    layout="centered"
)

# ------------------------------------------------------------
# CSS
# ------------------------------------------------------------
st.markdown("""
<style>
.main-title {
    text-align:center;
    font-size:2.5rem;
    font-weight:700;
    margin-bottom:5px;
}
.subtitle {
    text-align:center;
    color:#9ca3af;
    margin-bottom:30px;
}
.section {
    font-size:1.3rem;
    font-weight:650;
    margin:15px 0;
}
.divider {
    border-top:1px solid rgba(255,255,255,.15);
    margin:25px 0;
}

.footer {
    text-align: center;
    color: #6b7280;
    font-size: 0.8rem;
    margin-top: 30px;
    line-height: 1.8;
}

.footer span {
    color: #9ca3af;
    font-size: 0.75rem;
}
</style>
""", unsafe_allow_html=True)

# ------------------------------------------------------------
# LOAD MODEL
# ------------------------------------------------------------
@st.cache_resource
def load_model():
    model = joblib.load("LR_ford_car.pkl")
    scaler = joblib.load("scaler.pkl")
    columns = joblib.load("columns.pkl")
    return model, scaler, columns

@st.cache_data
def load_options():
    df = pd.read_csv("ford_car_dataset.csv")
    return (
        sorted(df["model"].dropna().unique()),
        sorted(df["transmission"].dropna().unique()),
        sorted(df["fuelType"].dropna().unique())
    )

try:
    model, scaler, columns = load_model()
    models, transmissions, fuels = load_options()

except FileNotFoundError:
    st.error(
        "Required files are missing. Make sure these files are "
        "in the same folder as app.py:"
    )
    st.code(
        "app.py\n"
        "ford_car_dataset.csv\n"
        "LR_ford_car.pkl\n"
        "scaler.pkl\n"
        "columns.pkl"
    )
    st.stop()

# ------------------------------------------------------------
# HEADER
# ------------------------------------------------------------
st.markdown(
    '<div class="main-title">🚗 Ford Car Price Predictor</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">AI-powered used Ford vehicle valuation</div>',
    unsafe_allow_html=True
)

# ------------------------------------------------------------
# VEHICLE INFORMATION
# ------------------------------------------------------------
st.markdown(
    '<div class="section">🚘 Vehicle Information</div>',
    unsafe_allow_html=True
)

c1, c2 = st.columns(2)

with c1:
    model_name = st.selectbox(
        "Car Model",
        models,
        index=models.index("Fiesta") if "Fiesta" in models else 0
    )

with c2:
    year = st.number_input(
        "Manufacturing Year",
        1990, 2026, 2018, 1
    )

c1, c2 = st.columns(2)

with c1:
    transmission = st.selectbox(
        "Transmission",
        transmissions,
        index=transmissions.index("Manual")
        if "Manual" in transmissions else 0
    )

with c2:
    fuel = st.selectbox(
        "Fuel Type",
        fuels,
        index=fuels.index("Petrol")
        if "Petrol" in fuels else 0
    )

# ------------------------------------------------------------
# TECHNICAL SPECIFICATIONS
# ------------------------------------------------------------
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

st.markdown(
    '<div class="section">⚙️ Technical Specifications</div>',
    unsafe_allow_html=True
)

c1, c2 = st.columns(2)

with c1:
    mileage = st.number_input(
        "Mileage",
        0, 300000, 25000, 1000
    )

with c2:
    engine = st.number_input(
        "Engine Size (Liters)",
        0.1, 6.0, 1.5, 0.1,
        format="%.1f"
    )

c1, c2 = st.columns(2)

with c1:
    mpg = st.number_input(
        "Miles Per Gallon (MPG)",
        10.0, 150.0, 55.0, 0.5
    )

with c2:
    tax = st.number_input(
        "Road Tax (£)",
        0, 1000, 145, 5
    )

# ------------------------------------------------------------
# BUTTONS
# ------------------------------------------------------------
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

c1, c2 = st.columns(2)

with c1:
    predict = st.button(
        "🚀 Predict Price",
        type="primary",
        width="stretch"
    )

with c2:
    reset = st.button(
        "🔄 Reset",
        width="stretch"
    )

if reset:
    st.rerun()

# ------------------------------------------------------------
# PREDICTION
# ------------------------------------------------------------
if predict:

    try:
        # Create empty input with EXACT training columns
        X = pd.DataFrame(
            0.0,
            index=[0],
            columns=columns
        )

        # -----------------------------
        # Numeric features
        # -----------------------------
        numeric_features = [
            "year",
            "mileage",
            "tax",
            "mpg",
            "engineSize"
        ]

        numeric_values = {
            "year": year,
            "mileage": mileage,
            "tax": tax,
            "mpg": mpg,
            "engineSize": engine
        }

        for feature in numeric_features:
            X.at[0, feature] = float(
                numeric_values[feature]
            )

        # -----------------------------
        # Categorical features
        # -----------------------------
        categorical_values = {
            "model": model_name,
            "transmission": transmission,
            "fuelType": fuel
        }

        for feature, value in categorical_values.items():

            dummy_column = f"{feature}_{value}"

            if dummy_column in X.columns:
                X.at[0, dummy_column] = 1.0

        # -----------------------------
        # Scale numeric features
        # -----------------------------
        X[numeric_features] = scaler.transform(
            X[numeric_features]
        )

        # -----------------------------
        # Predict
        # -----------------------------
        prediction = float(
            model.predict(X)[0]
        )

        # -----------------------------
        # Validate prediction
        # -----------------------------
        if prediction < 0:
            st.error(
                f"Invalid prediction returned by model: "
                f"£{prediction:,.2f}"
            )
            st.stop()

        # -----------------------------
        # Result
        # -----------------------------
        
        with st.container(border=True):
            st.markdown("### 💷 Estimated Market Value")
            st.markdown(
                f"# £{prediction:,.0f}"
            )
            st.caption("AI-powered price estimate")

        # -----------------------------
        # Summary
        # -----------------------------
        st.markdown("### 📋 Prediction Summary")

        c1, c2, c3, c4 = st.columns(4)

        c1.metric("Model", model_name)
        c2.metric("Year", year)
        c3.metric("Mileage", f"{mileage:,}")
        c4.metric("Engine", f"{engine:.1f} L")

        c1, c2 = st.columns(2)

        c1.metric("Transmission", transmission)
        c2.metric("Fuel Type", fuel)

    except Exception as e:

        st.error("❌ Prediction failed.")
        st.exception(e)
# ------------------------------------------------------------
# FOOTER
# ------------------------------------------------------------
st.markdown(
    """
    <div class="footer">
        Ford Car Price Predictor • Machine Learning Project<br>
        <span>Developed by Omkar V. Kinage</span>
    </div>
    """,
    unsafe_allow_html=True
)