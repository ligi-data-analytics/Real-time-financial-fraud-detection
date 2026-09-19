# Model Evaluation

## Fraud Detection Models

Two classification models were evaluated for the financial fraud detection task:

1. Logistic Regression — baseline model
2. LightGBM — tree-based model

The dataset was split using stratified sampling to preserve the fraud class distribution.

## Results

| Model               | Accuracy | Precision | Recall | F1 Score | ROC-AUC | PR-AUC |
| ------------------- | -------: | --------: | -----: | -------: | ------: | -----: |
| Logistic Regression |   0.2890 |    0.0437 | 0.9009 |   0.0834 |  0.5925 | 0.0438 |
| LightGBM            |   0.2315 |    0.0438 | 0.9782 |   0.0838 |  0.5943 | 0.0441 |

## Logistic Regression

The Logistic Regression model was used as the baseline.

* Accuracy: 28.90%
* Precision: 4.37%
* Recall: 90.09%
* F1 Score: 0.0834
* ROC-AUC: 0.5925
* PR-AUC: 0.0438

The model achieved high recall but generated a large number of false positives.

## LightGBM

A LightGBM classifier was trained using class weighting to address the highly imbalanced fraud dataset.

* Accuracy: 23.15%
* Precision: 4.38%
* Recall: 97.82%
* F1 Score: 0.0838
* ROC-AUC: 0.5943
* PR-AUC: 0.0441

The LightGBM model detected a larger proportion of fraudulent transactions, but also produced many false positives.

## Threshold Analysis

Different probability thresholds were evaluated for the LightGBM model.

At the default threshold of **0.50**:

* Precision: 4.38%
* Recall: 97.82%
* F1 Score: 0.0838

Increasing the threshold sharply reduced the number of predicted fraud cases. This indicates that threshold adjustment alone did not provide a substantial improvement in the current model.

## Feature Importance

The most influential features according to LightGBM feature importance included:

* `spending_deviation_score`
* `amount`
* `time_since_last_transaction`
* `geo_anomaly_score`
* `hour`
* `velocity_score`
* `sender_account_frequency`
* `receiver_account_frequency`
* `month`
* `day_of_week`

Feature importance represents how the model used the features during training and should not be interpreted as proof of causation.

## Conclusion

The initial modeling stage established a baseline and a tree-based model for fraud detection. The results show that the dataset is challenging because of severe class imbalance and limited model discrimination.

Further improvements can focus on feature engineering, model tuning, threshold optimization, and a production-oriented prediction pipeline.
