NUMERIC_FEATURES = [
    "LotArea",
    "GrLivArea",
    "TotalBsmtSF",
    "1stFlrSF",
    "2ndFlrSF",
    "GarageArea",
    "WoodDeckSF",
    "OpenPorchSF"
]

ORDINAL_CATEGORICAL_FEATURES = [
    "ExterQual",
    "ExterCond",
    "KitchenQual",
    "HeatingQC",
    "GarageQual",
    "GarageCond"
]

ORDINAL_NUMERIC_FEATURES = [
    "OverallQual",
    "OverallCond"
]

NOMINAL_FEATURES = [
    "Neighborhood",
    "MSZoning",
    "BldgType",
    "HouseStyle",
    "RoofStyle",
    "Exterior1st"
]

TEMPORAL_FEATURES = [
    "YearBuilt",
    "YearRemodAdd",
    "YrSold"
]

TEMPORAL_DERIVED_FEATURES = [
    "PropertyAge",
    "YearsSinceRemodel"
]

NUMERIC_FEATURES = NUMERIC_FEATURES + TEMPORAL_DERIVED_FEATURES
NUMERIC_FEATURES = NUMERIC_FEATURES + ORDINAL_NUMERIC_FEATURES
