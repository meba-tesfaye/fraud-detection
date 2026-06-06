# 🛡️ Real-Time Fraud Detection System for E-Commerce & Banking

A comprehensive machine learning pipeline designed to detect fraudulent transactions across two distinct data streams: E-commerce platforms and Bank Credit Card transactions. This repository contains the complete end-to-end data engineering, geolocation integration, and anti-leakage preprocessing pipelines for Task 1 (Interim-1).

---

## 📁 Repository Structure
The project is organized into a clean, modular layout following production data science best practices:

```text
├── data/
│   ├── raw/               # Raw immutable datasets (git-ignored)
│   └── processed/         # Cleaned, engineered, and scaled NumPy training/testing arrays
├── notebooks/
│   ├── eda-fraud-data.ipynb   # E-commerce pipeline (IP lookup, feature engineering, SMOTE)
│   └── eda-creditcard.ipynb   # Banking pipeline (Deduplication, scaling, SMOTE)
├── src/                   # Production script modules (for subsequent development)
├── .gitignore             # Formatted to protect raw data from leaking to GitHub
├── requirements.txt       # Verified dependency manifests (pandas, scikit-learn, imblearn, etc.)
└── README.md              # Project overview and documentation
