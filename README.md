# 🔐 AI-Powered Cybersecurity Threat Detection System

## 📌 Project Overview
This project is an AI-based cybersecurity system that detects network threats using machine learning. It analyzes network traffic data and identifies malicious activities such as intrusion and attacks. The system simulates a real Security Operations Center (SOC) environment.

---

## 🚀 Features
- Detects cyber threats using machine learning models
- Works on real-world network traffic dataset (NSL-KDD)
- Data preprocessing and feature engineering
- Model training and evaluation
- Real-time threat detection
- Interactive Streamlit dashboard
- Alert system for malicious activity

---

## 🧠 Technologies Used
- Python
- Pandas, NumPy
- Scikit-learn
- Streamlit
- Matplotlib
- Joblib

---

```

## 📁 Project Structure

AI-Cybersecurity-Threat-Detection/
│
├── dashboard/
│   └── app.py
│
├── data/
│   └── KDDTrain+.txt
│
├── models/
│   └── model.pkl
│
├── src/
│   ├── load_data.py
│   ├── clean_data.py
│   ├── feature_engineering.py
│   ├── model.py
│   ├── predict.py
│   └── evaluate.py
│
├── notebooks/
│   └── EDA.ipynb
│
├── outputs/
│   └── results.txt
│
├── images/
│   └── dashboard.png
│
├── docs/
│   └── project_report.md
│
├── main.py
├── requirements.txt
├── .gitignore
└── README.md

```

---

## ⚙️ How to Run the Project

### 1. Install Dependencies
pip install -r requirements.txt

### 2. Run the Dashboard
python -m streamlit run dashboard/app.py

---

## 📊 Output
- Displays uploaded network data
- Shows predictions for each record
- Alerts if threat is detected
- Visualizes prediction results

---

## 🎯 Use Cases
- Intrusion Detection Systems (IDS)
- Network Security Monitoring
- Cyber Threat Analysis
- SOC (Security Operations Center) Simulation

---

## 🧠 Key Concepts Used
- Machine Learning (Random Forest)
- Anomaly Detection
- Data Preprocessing
- Feature Engineering
- Model Deployment

---

## 👩‍💻 Author
- Saloni Keshkar

---

## ⭐ Future Improvements
- Add deep learning models (LSTM, Autoencoders)
- Real-time packet capture integration
- API-based threat detection
- Advanced dashboard with analytics