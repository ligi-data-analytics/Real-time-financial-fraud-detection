# 💳 Real-Time Financial Fraud Detection

A machine learning-based financial fraud detection project developed to identify potentially fraudulent transactions using **LightGBM**, with a **FastAPI REST API** for transaction-level prediction and **Docker** configuration for deployment.

> **Current implementation:** Machine Learning + FastAPI + Docker
> **Future enhancement:** Kafka + Spark Structured Streaming for real-time transaction processing.

---

## 📌 Project Overview

Financial fraud detection is an important application of machine learning where the objective is to identify suspicious transactions while minimizing missed fraudulent transactions.

This project uses a large-scale financial transaction dataset containing **5 million records** to build a fraud detection model.

The project covers:

* Data exploration and cleaning
* Feature engineering
* Fraud pattern analysis
* Machine learning model development
* Fraud probability prediction
* REST API development using FastAPI
* Docker containerization
* GitHub-based project documentation

---

## 📊 Dataset

The dataset contains approximately **5 million financial transactions** and includes transaction, customer, device, location, payment and fraud-related information.

### Dataset characteristics

* **Rows:** 5,000,000
* **Features:** 18 original features
* **Target:** `is_fraud`
* **Fraud transactions:** ~3.59%
* **Non-fraud transactions:** ~96.41%

The dataset is highly imbalanced, which makes fraud detection and false-negative reduction important considerations during model development.

---

## 🔍 Exploratory Data Analysis

The project includes analysis of:

* Fraud vs. non-fraud transaction distribution
* Transaction amounts
* Transaction types
* Merchant categories
* Payment channels
* Device and location information
* Transaction timing
* Fraud-related behavioral patterns

---

## 🛠️ Data Preprocessing & Feature Engineering

The preprocessing workflow includes:

* Handling missing values
* Handling invalid transaction timestamps
* Handling invalid/negative transaction intervals
* Encoding categorical variables
* Frequency-based encoding for selected high-cardinality features
* Timestamp feature extraction

### Created time-based features

* `hour`
* `day_of_week`
* `month`
* `is_weekend`

These features help the model identify transaction behavior patterns associated with fraudulent activity.

---

## 🤖 Machine Learning Model

### LightGBM

The final fraud detection model was developed using **LightGBM**, a gradient boosting framework suitable for large tabular datasets.

The trained model is saved as:

```text
fraud_detection_lgbm_model.pkl
```

The model produces:

* Fraud / Non-Fraud prediction
* Fraud probability

Example:

```text
Transaction ID: T107720
Prediction: Fraud
Fraud Probability: 55.02%
```

---

## 🚀 FastAPI REST API

The trained model was integrated into a **FastAPI REST API** to allow transaction-level fraud prediction.

### API Endpoints

| Endpoint   | Method | Description               |
| ---------- | ------ | ------------------------- |
| `/`        | GET    | API health/status check   |
| `/predict` | POST   | Predict transaction fraud |

### API Workflow

```text
Transaction Input
       ↓
FastAPI Request Validation
       ↓
Feature Preprocessing
       ↓
LightGBM Model
       ↓
Fraud Prediction
       ↓
Fraud Probability
```

The API uses **Pydantic** for request validation and automatically performs the required feature preprocessing before generating predictions.

---

## 🐳 Docker

The application has been prepared for containerized deployment using Docker.

### Docker configuration

```text
Dockerfile
requirements.txt
app.py
fraud_detection_lgbm_model.pkl
preprocessing_mappings.pkl
```

The Docker container is configured to run the FastAPI application using Uvicorn on port `8000`.

Example command:

```bash
uvicorn app:app --host 0.0.0.0 --port 8000
```

---

## 📁 Project Structure

```text
Real-time-financial-fraud-detection/
│
├── 01_EDA.ipynb
│
├── app.py
├── fraud_detection_lgbm_model.pkl
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── .gitignore
│
└── README.md
```

> `preprocessing_mappings.pkl` is required by the API but is not stored directly in GitHub because of its large file size.

---

## 🏗️ Current Architecture

```text
Financial Transaction Dataset
            ↓
     Data Cleaning & EDA
            ↓
     Feature Engineering
            ↓
     LightGBM Model
            ↓
     Model Evaluation
            ↓
       FastAPI API
            ↓
     Docker Container
```

---

## 🔮 Future Enhancement: Real-Time Streaming

The current implementation provides the **machine learning and API foundation** for a real-time fraud detection system.

The next stage can extend the architecture using:

```text
Transaction Source
       ↓
Apache Kafka
       ↓
Spark Structured Streaming
       ↓
Fraud Detection Model
       ↓
Fraud Alerts
       ↓
Cassandra / Database
       ↓
Grafana / Power BI
```

### Planned technologies

* **Apache Kafka** – transaction/event streaming
* **Apache Spark Structured Streaming** – real-time processing
* **Machine Learning** – fraud prediction
* **Cassandra** – fraud alert storage
* **Grafana** – real-time operational monitoring
* **Power BI** – business-level fraud analysis and reporting

These components represent the planned streaming extension and are **not part of the current completed implementation**.

---

## 🎯 Project Objective

The objective of this project is to demonstrate an end-to-end machine learning workflow for financial fraud detection, from data preparation and model development to API-based prediction and deployment preparation.

The project also provides a foundation that can be extended into a **Kafka + Spark real-time fraud detection architecture**.

---

## 💡 Key Skills Demonstrated

* Python
* Pandas
* NumPy
* Scikit-learn
* LightGBM
* Exploratory Data Analysis
* Feature Engineering
* Imbalanced Classification
* Machine Learning
* FastAPI
* REST API
* Pydantic
* Uvicorn
* Docker
* Git & GitHub
* ML Model Deployment

---

## 📌 Project Status

| Component                  | Status                |
| -------------------------- | --------------------- |
| Data Cleaning              | ✅ Completed           |
| Exploratory Data Analysis  | ✅ Completed           |
| Feature Engineering        | ✅ Completed           |
| LightGBM Model             | ✅ Completed           |
| Model Serialization        | ✅ Completed           |
| FastAPI API                | ✅ Completed           |
| API Testing                | ✅ Completed           |
| Docker Configuration       | ✅ Completed           |
| GitHub Documentation       | ✅ Completed           |
| Kafka Streaming            | 🔮 Future Enhancement |
| Spark Structured Streaming | 🔮 Future Enhancement |
| Cassandra                  | 🔮 Future Enhancement |
| Grafana                    | 🔮 Future Enhancement |

---

## 👩‍💻 Author

**Ligi Mathew**

Data Analytics | Python | SQL | Excel | Power BI | Machine Learning

---

### ⭐ Final Note

This project demonstrates the complete **ML → API → deployment preparation** workflow and is designed as a foundation for extending into a production-style real-time financial fraud detection system using Kafka and Spark.
