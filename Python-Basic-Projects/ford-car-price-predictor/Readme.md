# 🚗 Ford Car Price Predictor

**My first Machine Learning project** — a web application that predicts the estimated price of a used Ford car based on its specifications.

## ✨ Features

🚘 Car Model  
📅 Manufacturing Year  
🛣️ Mileage  
⚙️ Engine Size  
🔧 Transmission  
⛽ Fuel Type  
📈 MPG  
💷 Road Tax  

Click **🚀 Predict Price** to get an estimated market value.

## 🧠 How It Works

~~~text
Ford Dataset
     ↓
Data Preprocessing
     ↓
Feature Scaling
     ↓
Linear Regression Model
     ↓
Price Prediction
     ↓
Streamlit Web App
~~~

## 📊 Model Performance

| Metric | Result |
|---|---:|
| Algorithm | Linear Regression |
| R² Score | 0.819 |
| MAE | £1,361 |
| RMSE | £2,015 |

> ⚠️ The predicted value is an ML-based estimate and is not a guaranteed market price.

## 🛠️ Technologies

`Python` • `Pandas` • `NumPy` • `Scikit-learn` • `Joblib` • `Streamlit`

## 📁 Project Structure

~~~text
ford-car-price-predictor/
│
├── app.py
├── ford_car_dataset.csv
├── LR_ford_car.pkl
├── scaler.pkl
├── columns.pkl
├── Ford_Car_Price_Pred_(1).ipynb
└── README.md
~~~

## 🌐 Live Demo

👉 **[Try the Ford Car Price Predictor](https://car-price-predictorr-ok-1lr.streamlit.app/)**

## 🚀 Run Locally

### 1. Clone the repository

~~~bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd ML_Model_1
~~~

### 2. Install dependencies

~~~bash
pip install pandas numpy scikit-learn matplotlib seaborn joblib streamlit
~~~

### 3. Start the application

~~~bash
streamlit run app.py
~~~

The app will normally open at:

`http://localhost:8501`

## 💡 What I Learned

This project helped me understand the complete Machine Learning workflow:

**Data → Preprocessing → Training → Evaluation → Deployment**

It was my first experience taking a trained ML model and turning it into a working web application.

## 🚧 What's Next

Exploring advanced regression models and better feature engineering to improve prediction performance.

## 👨‍💻 Developer

**Omkar V. Kinage**

*First Machine Learning Project*

⭐ If you find this project interesting, consider starring the repository.
