import streamlit as st
import pandas as pd
import joblib

# Load model
@st.cache_resource
def load_model():
    return joblib.load("fraud_detection.pkl")

model = load_model()

# Required features for the model
required_fields = {
    "step":None,
    "type": None,
    "amount": None,
    "oldbalanceOrg": None,
    "newbalanceOrig": None,
    "oldbalanceDest": None,
    "newbalanceDest": None
}

# Streamlit UI
st.set_page_config(page_title="💳 Fraud Detection App", layout="centered")
st.title("🔍 Fraud Detection on Transactions")
st.markdown("Upload your CSV, map the correct columns, or enter a manual transaction to detect **fraudulent** behavior.")

# File uploader
uploaded_file = st.file_uploader("📤 Upload your CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.success("✅ File uploaded successfully!")
    st.subheader("📄 Preview")
    st.dataframe(df.head())

    st.subheader("🧩 Map Your Columns")
    st.markdown("Match your column names to the model’s expected inputs:")

    # Column mapping using dropdowns
    col_map = {}
    for key in required_fields.keys():
        col_map[key] = st.selectbox(
            f"Select column for **{key}**",
            options=df.columns,
            key=key
        )

    # Submit button
    if st.button("🚀 Run Prediction"):
        try:
            input_data = df[[col_map[key] for key in required_fields.keys()]].copy()
            input_data.columns = list(required_fields.keys())  # Rename for model

            prediction = model.predict(input_data)
            df["is_fraud"] = prediction

            st.subheader("✅ Prediction Results")
            st.dataframe(df)

            st.download_button(
                "⬇️ Download CSV with Predictions",
                data=df.to_csv(index=False).encode("utf-8"),
                file_name="fraud_predictions.csv",
                mime="text/csv"
            )
        except Exception as e:
            st.error("error")

# Manual input option
st.subheader("✍️ Manually Enter a Transaction")
manual_type = st.selectbox("Transaction Type", ['PAYMENT', 'TRANSFER', 'CASH_OUT', 'DEBIT', 'CASH_IN'])
manual_amount = st.number_input("Amount", min_value=0.0, step=0.01)
manual_oldbalanceOrg = st.number_input("Old Balance (Origin)", min_value=0.0, step=0.01)
manual_newbalanceOrig = st.number_input("New Balance (Origin)", min_value=0.0, step=0.01)
manual_oldbalanceDest = st.number_input("Old Balance (Destination)", min_value=0.0, step=0.01)
manual_newbalanceDest = st.number_input("New Balance (Destination)", min_value=0.0, step=0.01)

if st.button("🔎 Predict Single Transaction"):
    try:
        single_df = pd.DataFrame([{
            
            "type": manual_type,
            "amount": manual_amount,
            "oldbalanceOrg": manual_oldbalanceOrg,
            "newbalanceOrig": manual_newbalanceOrig,
            "oldbalanceDest": manual_oldbalanceDest,
            "newbalanceDest": manual_newbalanceDest
        }])

        result = model.predict(single_df)
        st.success(f" Prediction: {'❌FRAUD' if result[0] == 1 else '♏♏✅NOT FRAUD'}")
        st.dataframe(single_df.assign(is_fraud=result[0]))

    except Exception as e:
        st.error(f"❌ Error: {e}")
