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

ORDINAL_FEATURES = [
    "OverallQual",
    "OverallCond",
    "ExterQual",
    "ExterCond",
    "KitchenQual",
    "HeatingQC",
    "GarageQual",
    "GarageCond"
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
