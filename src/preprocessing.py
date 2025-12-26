from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder, FunctionTransformer
from sklearn.impute import SimpleImputer
from src.preprocessing_utils import cast_to_string

from src.features import (
    NUMERIC_FEATURES,
    ORDINAL_CATEGORICAL_FEATURES,
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
    ]

    return Pipeline(steps=[
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("to_str", FunctionTransformer(cast_to_string)),
        ("encoder", OrdinalEncoder(
            categories=ordinal_categories,
            handle_unknown="use_encoded_value",
            unknown_value=-1
        ))
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
            ("ord", build_ordinal_pipeline(), ORDINAL_CATEGORICAL_FEATURES),
            ("nom", build_nominal_pipeline(), NOMINAL_FEATURES)
        ],
        remainder="drop"
    )
