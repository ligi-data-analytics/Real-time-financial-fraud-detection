# API Testing

## Overview

The FastAPI application was tested using a balanced sample of 40 real transactions from the financial fraud detection dataset.

The test included:

- 20 actual non-fraud transactions
- 20 actual fraud transactions

## Results

| Metric | Result |
|---|---:|
| Total transactions | 40 |
| Actual fraud | 20 |
| Actual non-fraud | 20 |
| Correct predictions | 40 |
| Incorrect predictions | 0 |
| Accuracy | 1.00 |
| Fraud Precision | 1.00 |
| Fraud Recall | 1.00 |
| Fraud F1 Score | 1.00 |

## Confusion Matrix

| Actual / Predicted | Not Fraud | Fraud |
|---|---:|---:|
| Not Fraud | 20 | 0 |
| Fraud | 0 | 20 |

## Interpretation

The API correctly processed all 40 transactions in this validation sample.

All 20 non-fraud transactions were classified as Not Fraud, and all 20 fraud transactions were classified as Fraud.

This confirms that the FastAPI endpoint and the preprocessing/model pipeline are working correctly for this test sample.

### Important Note

The 100% result applies only to this 40-transaction API validation sample. It should not be interpreted as the overall performance of the fraud detection model.

The full test-set model evaluation is documented separately in `docs/model_evaluation.md`.
