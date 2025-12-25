from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder
from sklearn.impute import SimpleImputer

from src.features import (
    NUMERIC_FEATURES,
    ORDINAL_FEATURES,
    NOMINAL_FEATURES
)

def build_numeric_pipeline():
    return Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='median')),
    ])

def build_ordinal_pipeline():
    ordinal_categories = [
        ["Po", "Fa", "TA", "Gd", "Ex"],
        ["Po", "Fa", "TA", "Gd", "Ex"],
        ["Po", "Fa", "TA", "Gd", "Ex"],
        ["Po", "Fa", "TA", "Gd", "Ex"],
        ["Po", "Fa", "TA", "Gd", "Ex"],
        ["Po", "Fa", "TA", "Gd", "Ex"],
        ["Po", "Fa", "TA", "Gd", "Ex"],
        ["Po", "Fa", "TA", "Gd", "Ex"]
    ]

    return Pipeline(steps=[
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("encoder", OrdinalEncoder(categories=ordinal_categories))
    ])

def build_nominal_pipeline():
    return Pipeline(steps=[
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("encoder", OneHotEncoder(handle_unknown="ignore"))
    ])

def build_preprocessor():
    return ColumnTransformer(
        transformers=[
            ("num", build_numeric_pipeline(), NUMERIC_FEATURES),
            ("ord", build_ordinal_pipeline(), ORDINAL_FEATURES),
            ("nom", build_nominal_pipeline(), NOMINAL_FEATURES)
        ],
        remainder="drop"
    )
