# Fraud Detection System for E-Commerce and Banking

**Author:** Eyu Birhanu  
**Organization:** Adey Innovations Inc.  
**Date:** December 2025  

## 📌 Project Overview
This project focuses on building a robust machine learning pipeline to detect fraudulent transactions in e-commerce and banking data. The goal is to identify fraudulent activities accurately while minimizing false positives, ensuring a balance between security and user experience.

The system handles two distinct datasets:
1.  **Fraud_Data.csv:** E-commerce transaction data requiring geolocation analysis and pattern recognition.
2.  **CreditCard.csv:** Bank transaction data involving PCA-transformed features.

## 📂 Project Structure
The repository is organized to ensure reproducibility and modularity:

```text
fraud-detection/
├── .github/workflows/    # CI/CD configurations
├── data/                 # Raw and processed data (Not synced to Git)
├── models/               # Saved model artifacts
├── notebooks/            # Jupyter Notebooks for analysis and experiments
│   ├── eda-fraud-data.ipynb   # Task 1: EDA and Preprocessing
│   └── modeling.ipynb         # Task 2: Model Training & Evaluation
├── src/                  # Source code for production pipelines
│   ├── preprocess.py     # Data cleaning, feature engineering, and geolocation merge
├── tests/                # Unit tests
├── .gitignore            # Files to ignore (e.g., large datasets)
├── README.md             # Project documentation
└── requirements.txt      # Python dependencies
```

## 🚀 Key Features & Methodology (Interim Status)

### 1. Data Analysis & Preprocessing
*   **Geolocation Mapping:** Converted IP addresses to integer formats and merged with `IpAddress_to_Country.csv` using efficient range matching (`merge_asof`).
*   **Feature Engineering:**
    *   `time_since_signup`: Calculated the seconds between signup and purchase. Insight: Fraudulent transactions often happen almost immediately after signup.
    *   `hour_of_day` & `day_of_week`: Extracted to capture temporal fraud patterns.
*   **Data Cleaning:** Handled missing values and duplicates programmatically in `src/preprocess.py`.

### 2. Machine Learning Modeling
*   **Handling Class Imbalance:** The dataset is highly imbalanced (legitimate transactions far outnumber fraud). We implemented **SMOTE** (Synthetic Minority Over-sampling Technique) within an `imbalanced-learn` pipeline to oversample the minority class during training only.
*   **Model Selection:** Currently using a **Random Forest Classifier** as a robust baseline.
*   **Evaluation Metrics:** Focused on Precision-Recall metrics (**AUPRC**, **F1-Score**) rather than simple accuracy, which can be misleading in fraud detection.

## 📊 Current Performance (Interim Results)
Based on the Random Forest model trained on E-commerce data:

| Metric | Score | Interpretation |
| :--- | :--- | :--- |
| **Precision (Fraud)** | 0.82 | When the model flags a transaction, it is correct 82% of the time. |
| **Recall (Fraud)** | 0.53 | The model successfully catches 53% of all fraud cases. |
| **AUPRC** | 0.696 | Area Under Precision-Recall Curve (Good baseline performance). |

## 🛠️ Installation & Usage

**1. Clone the repository:**
```bash
git clone https://github.com/eyuBirhanu/fraud-detection.git
cd fraud-detection
```

**2. Install Dependencies:**
```bash
pip install -r requirements.txt
```

**3. Run the Analysis:**
*   To see the Data Analysis: Open `notebooks/eda-fraud-data.ipynb`
*   To run the Model: Open `notebooks/modeling.ipynb`