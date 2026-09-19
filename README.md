# Real-time-financial-fraud-detection
Real-time financial fraud detection pipeline using Kafka, Spark Structured Streaming, machine learning, and NoSQL for anomaly detection and fraud alerting.
## Exploratory Data Analysis (EDA)

The financial fraud detection dataset contains **5,000,000 transactions** with **18 columns** covering transaction details, customer accounts, device information, location, payment channels, and fraud indicators.

### Dataset Overview

* **Total transactions:** 5,000,000
* **Total columns:** 18
* **Duplicate rows:** 0
* **Duplicate transaction IDs:** 0
* **Fraud transactions:** 179,553 (3.59%)
* **Non-fraud transactions:** 4,820,447 (96.41%)

### Data Quality Findings

The dataset contains missing values in two important columns:

| Column                        | Missing Values | Percentage |
| ----------------------------- | -------------: | ---------: |
| `fraud_type`                  |      4,820,447 |     96.41% |
| `time_since_last_transaction` |        896,513 |     17.93% |

The `fraud_type` column was excluded from modeling because it is highly correlated with the target and would introduce target leakage.

### Transaction Time Analysis

The original `timestamp` column was converted into useful time-based features:

* Hour
* Day of week
* Month
* Weekend indicator

Three invalid timestamp values were identified and handled during preprocessing.

### Data Preprocessing

The following preprocessing techniques were applied:

* Removed `transaction_id` from model features.
* Converted invalid negative values in `time_since_last_transaction` to missing values.
* Created missing-value and invalid-value indicators.
* Median-imputed valid missing time values.
* Applied frequency encoding to high-cardinality account, IP, and device fields.
* Applied one-hot encoding to categorical variables.
* Used a stratified train/test split to preserve the fraud ratio.

### Key EDA Observation

The dataset is highly imbalanced, with fraud transactions representing only **3.59%** of all transactions. Therefore, accuracy alone is not sufficient for evaluating fraud detection models. Precision, recall, F1-score, ROC-AUC, and PR-AUC are also considered.
