# Fraud Detection System for E-Commerce and Banking

**Author:** Eyu Birhanu  
**Organization:** Adey Innovations Inc.  
**Date:** December 30, 2025  

## 📌 Project Overview
This project is a comprehensive Machine Learning solution designed to detect fraudulent transactions in two critical financial sectors:
1.  **E-Commerce:** Identifying fraudulent purchases using geolocation and behavioral patterns.
2.  **Banking:** Detecting credit card fraud using PCA-transformed financial data.

The system emphasizes **Explainable AI (XAI)** to ensure transparency in decision-making, allowing business stakeholders to understand *why* a transaction was flagged.

## 📂 Project Structure
```text
fraud-detection/
├── .github/workflows/    # CI/CD pipelines
├── data/                 # Raw and processed datasets (Ignored in Git)
├── models/               # Serialized model artifacts
├── notebooks/            # Analysis & Experimentation
│   ├── eda-fraud-data.ipynb       # Task 1: E-commerce EDA & Preprocessing
│   ├── eda-creditcard.ipynb       # Task 2: Bank Data Analysis
│   ├── modeling.ipynb             # Task 3: Model Training & Comparison
│   └── shap-explainability.ipynb  # Task 4: SHAP Explainability
├── reports/              # Final PDF Report and figures
├── src/                  # Production Source Code
│   ├── preprocess.py     # Data pipeline & Geolocation logic
├── tests/                # Unit Tests
├── .gitignore            # Git configuration
├── README.md             # Project Documentation
└── requirements.txt      # Dependencies
```

## 🚀 Key Features

### 1. Advanced Preprocessing
*   **Geolocation Integration:** Efficiently merged IP addresses with country data using `merge_asof` for high-speed range lookups.
*   **Behavioral Features:** Calculated `Time_Since_Signup` to detect bot-like "signup-and-buy" patterns.
*   **Robust Scaling:** Handled financial outliers in credit card data using `RobustScaler`.

### 2. Machine Learning Pipeline
*   **Imbalance Handling:** Utilized SMOTE (Synthetic Minority Over-sampling Technique) within a Stratified Cross-Validation pipeline to prevent overfitting.
*   **Model Comparison:** Systematically evaluated three architectures:
    *   Logistic Regression (Baseline)
    *   Random Forest (Selected Champion)
    *   XGBoost (Gradient Boosting)

### 3. Explainability (SHAP)
*   Implemented **SHAP (SHapley Additive exPlanations)** to visualize feature importance.
*   **Key Insight:** The interval between account creation and the first transaction is the single strongest predictor of fraud.

## 📊 Final Results

### E-Commerce Model Performance (Random Forest)
| Metric | Score | Interpretation |
| :--- | :--- | :--- |
| **Precision** | 0.82 | 82% of flagged transactions are actual fraud (Low False Positives). |
| **Recall** | 0.53 | Detects ~53% of all fraud cases. |
| **AUPRC** | 0.70 | Strong performance for highly imbalanced data. |

### Credit Card Model Performance
Successfully generalized to banking data with an **AUPRC > 0.80**.

## 🛠️ Setup & Installation

### Clone the Repository
```bash
git clone https://github.com/eyuBirhanu/fraud-detection.git
cd fraud-detection
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Run Tests
```bash
python -m unittest tests/test_preprocess.py
```

### Explore the Notebooks
Start with `notebooks/shap-explainability.ipynb` to see the final insights.