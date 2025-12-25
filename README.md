# House Price Prediction — End-to-End Machine Learning Pipeline

## Project Overview
This project implements an end-to-end machine learning pipeline to predict
residential house prices based on structural, temporal and location features.

The focus of this project is not only predictive performance, but also
engineering best practices such as:
- Semantic feature handling
- Data leakage prevention
- Reproducible preprocessing pipelines
- Fair model comparison

---

## Problem Statement
Given historical housing data, the objective is to predict the final sale
price of a house while ensuring robustness, stability and interpretability
of the modeling process.

This is formulated as a supervised regression problem.

---

## Dataset
The project uses the Ames Housing dataset, which contains a wide range of
numerical, ordinal and categorical features describing residential properties.

Key challenges of the dataset include:
- High-cardinality categorical variables
- Ordinal features with semantic ordering
- Missing values representing both absence and unknown information
- Strong target skewness

---

## Project Structure
* data/ — Raw and processed datasets
* notebooks/ — Step-by-step analysis and modeling notebooks
* src/ — Reusable preprocessing pipeline
* requirements.txt — Project dependencies


---

## Methodology

### 1. Exploratory Data Analysis
- Target distribution analysis and skewness evaluation
- Semantic classification of features
- Domain-aware missing value analysis
- Outlier inspection without aggressive removal

### 2. Preprocessing & Feature Engineering
- Separation of numerical, ordinal and nominal features
- Explicit ordinal encoding with semantic ordering
- Robust handling of missing values
- Temporal feature engineering (e.g. property age)
- End-to-end preprocessing pipeline using `ColumnTransformer`

### 3. Modeling
Models were trained and compared using the same preprocessing pipeline
and cross-validation strategy:

- Ridge Regression (baseline)
- Random Forest Regressor
- Gradient Boosting Regressor

A logarithmic transformation of the target variable was applied to improve
stability and error distribution.

### 4. Evaluation
- Cross-validated RMSE comparison
- Residual analysis to detect bias and heteroscedasticity
- Final model selection based on performance and stability

---

## Models & Results
The Random Forest model was selected as the final model due to its strong
performance and superior stability across cross-validation folds.

---

## Key Engineering Decisions
- No data leakage between training and test sets
- Semantic handling of missing values
- Ordinal features encoded with explicit ordering
- Centralized training logic for fair model comparison
- Clear separation between exploration and system code

---

## How to Run
1. Install dependencies
2. Run notebooks in order:
   - `01_eda.ipynb`
   - `02_preprocessing.ipynb`
   - `03_modeling.ipynb`
   - `04_evaluation.ipynb`

---

## Future Improvements
- Hyperparameter optimization
- Model persistence and inference pipeline
- Feature importance and explainability (e.g. SHAP)
- API deployment for real-time predictions
