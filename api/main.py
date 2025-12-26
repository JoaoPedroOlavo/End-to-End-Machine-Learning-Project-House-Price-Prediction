from fastapi import FastAPI
from pydantic import BaseModel, Field
import pandas as pd

import sys
from pathlib import Path

from src.predict import predict_price

# Garantir que o src esteja no path
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(PROJECT_ROOT))

app = FastAPI(
    title="House Price Prediction API",
    description="Predict house prices using a trained ML pipeline",
    version="1.0.0"
)

class HouseInput(BaseModel):
    LotArea: int
    GrLivArea: int
    TotalBsmtSF: int
    FirstFlrSF: int = Field(..., alias="1stFlrSF")
    SecondFlrSF: int = Field(..., alias="2ndFlrSF")
    GarageArea: int
    WoodDeckSF: int
    OpenPorchSF: int

    OverallQual: int
    OverallCond: int

    ExterQual: str
    ExterCond: str
    KitchenQual: str
    HeatingQC: str
    GarageQual: str
    GarageCond: str

    Neighborhood: str
    MSZoning: str
    BldgType: str
    HouseStyle: str
    RoofStyle: str
    Exterior1st: str

    YearBuilt: int
    YearRemodAdd: int
    YrSold: int

    class Config:
        allow_population_by_field_name = True

@app.get("/")
def health_check():
    return {"status": "API is running"}

@app.post("/predict")
def predict(input_data: HouseInput):
    data_dict = input_data.dict(by_alias=True)
    df = pd.DataFrame([data_dict])

    prediction = predict_price(df)

    return {
        "predicted_price": float(prediction[0])
    }