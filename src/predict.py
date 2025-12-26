import joblib
import pandas as pd
import numpy as np

from src.temporal import add_temporal_features
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
MODEL_PATH = PROJECT_ROOT / "models" / "house_price_models.joblib"


def load_model():
    """
    Load the trained machine learning pipeline from disk.
    """
    if not MODEL_PATH.exists():
        raise FileNotFoundError(f"Model file not found at: {MODEL_PATH}")

    return joblib.load(MODEL_PATH)



def predict_price(input_data: pd.DataFrame):
    """
    Predict house prices given raw input data.
    """
    model = load_model()

    input_data = add_temporal_features(input_data)

    log_prediction = model.predict(input_data)
    prediction = np.expm1(log_prediction)

    return prediction
