
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import pandas as pd
import numpy as np
import joblib

# --------------------------------------------------
# Load model and preprocessing data
# --------------------------------------------------

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_PATH = os.path.join(
    BASE_DIR,
    "fraud_detection_lgbm_model.pkl"
)

PREPROCESSING_PATH = os.path.join(
    BASE_DIR,
    "preprocessing_mappings.pkl"
)

loaded_model = joblib.load(MODEL_PATH)
preprocessing_data = joblib.load(PREPROCESSING_PATH)


# --------------------------------------------------
# FastAPI application
# --------------------------------------------------

app = FastAPI(
    title="Real-Time Financial Fraud Detection API",
    description="API for predicting fraudulent financial transactions.",
    version="1.0.0"
)


# --------------------------------------------------
# Transaction input schema
# --------------------------------------------------

class TransactionInput(BaseModel):
    transaction_id: str
    timestamp: str
    sender_account: str
    receiver_account: str
    amount: float
    transaction_type: str
    merchant_category: str
    location: str
    device_used: str
    time_since_last_transaction: Optional[float] = None
    spending_deviation_score: float
    velocity_score: int
    geo_anomaly_score: float
    payment_channel: str
    ip_address: str
    device_hash: str


# --------------------------------------------------
# Health check
# --------------------------------------------------

@app.get("/")
def home():
    return {
        "message": "Financial Fraud Detection API is running",
        "status": "success"
    }


# --------------------------------------------------
# Prediction endpoint
# --------------------------------------------------

@app.post("/predict")
def predict_fraud(transaction: TransactionInput):

    row = pd.DataFrame([transaction.model_dump()])

    row["timestamp"] = pd.to_datetime(
        row["timestamp"],
        errors="coerce"
    )

    row["hour"] = row["timestamp"].dt.hour
    row["day_of_week"] = row["timestamp"].dt.dayofweek
    row["month"] = row["timestamp"].dt.month
    row["is_weekend"] = (
        row["day_of_week"] >= 5
    ).astype(int)

    row["sender_account_frequency"] = (
        row["sender_account"]
        .map(preprocessing_data["sender_frequency"])
        .fillna(0)
    )

    row["receiver_account_frequency"] = (
        row["receiver_account"]
        .map(preprocessing_data["receiver_frequency"])
        .fillna(0)
    )

    row["ip_address_frequency"] = (
        row["ip_address"]
        .map(preprocessing_data["ip_frequency"])
        .fillna(0)
    )

    row["device_hash_frequency"] = (
        row["device_hash"]
        .map(preprocessing_data["device_frequency"])
        .fillna(0)
    )

    row["time_since_last_transaction_missing"] = (
        row["time_since_last_transaction"]
        .isna()
        .astype(int)
    )

    row["time_since_last_transaction_invalid"] = (
        row["time_since_last_transaction"] < 0
    ).fillna(False).astype(int)

    row.loc[
        row["time_since_last_transaction"] < 0,
        "time_since_last_transaction"
    ] = np.nan

    row["time_since_last_transaction"] = (
        row["time_since_last_transaction"]
        .fillna(
            preprocessing_data[
                "median_time_since_last_transaction"
            ]
        )
    )

    categorical_columns = [
        "transaction_type",
        "merchant_category",
        "location",
        "device_used",
        "payment_channel"
    ]

    row_encoded = pd.get_dummies(
        row,
        columns=categorical_columns,
        drop_first=True,
        dtype=int
    )

    prediction_input = row_encoded.reindex(
        columns=loaded_model.feature_name_,
        fill_value=0
    )

    prediction = loaded_model.predict(
        prediction_input
    )[0]

    probability = float(
        loaded_model.predict_proba(
            prediction_input
        )[0][1]
    )

    result = "Fraud" if prediction else "Not Fraud"

    return {
        "transaction_id": transaction.transaction_id,
        "prediction": result,
        "fraud_probability": round(
            probability * 100,
            2
        )
    }
