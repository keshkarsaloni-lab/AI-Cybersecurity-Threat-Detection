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
## 📁 Project Structure

AI-Cybersecurity-Threat-Detection/
│
├── dashboard/                  # Streamlit dashboard UI
│   └── app.py
│
├── data/                       # Raw dataset
│   └── KDDTrain+.txt
│
├── models/                     # Saved trained models
│   └── model.pkl
│
├── src/                        # Core ML pipeline code
│   ├── load_data.py            # Load dataset
│   ├── clean_data.py           # Data cleaning
│   ├── feature_engineering.py  # Feature creation & encoding
│   ├── model.py                # Model training
│   ├── predict.py              # Predictions
│   └── evaluate.py             # Evaluation metrics
│
├── notebooks/                  # Jupyter notebooks (EDA)
│   └── EDA.ipynb
│
├── outputs/                    # Results and logs
│   └── results.txt
│
├── images/                     # Screenshots for README
│   └── dashboard.png
│
├── docs/                       # Project documentation
│   └── project_report.md
│
├── main.py                     # Main execution script
├── requirements.txt            # Dependencies
├── .gitignore                  # Ignored files
└── README.md                   # Project documentation

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