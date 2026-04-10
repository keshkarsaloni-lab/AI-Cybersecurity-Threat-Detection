import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder

st.title("🔐 AI Cybersecurity Threat Detection System")

# Load model
model = joblib.load("models/model.pkl")

uploaded_file = st.file_uploader("Upload CSV", type=["csv", "txt"])

if uploaded_file:
    df = pd.read_csv(uploaded_file, header=None)

    st.write("Uploaded Data:")
    st.dataframe(df.head())

    # Feature Engineering (same as training)
    le = LabelEncoder()
    for col in df.columns:
        try:
            df[col] = le.fit_transform(df[col])
        except:
            pass

    # Split (same as training)
    X = df.iloc[:, :-1]

    # Predict
    predictions = model.predict(X)

    st.write("Predictions:")
    st.write(predictions)

    # Threat detection
    if (predictions > 0).any():
        st.error("⚠ Threat Detected!")
    else:
        st.success("✅ No Threat Detected")

    # Graph
    st.write("Prediction Distribution")
    plt.hist(predictions)
    st.pyplot(plt)