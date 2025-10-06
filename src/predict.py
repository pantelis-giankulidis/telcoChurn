import joblib
import numpy as np
import pandas as pd

MODEL_PATH = 'models/model.pkl'

class Predictor:
    def __init__(self, model_path=MODEL_PATH):
        self.model = joblib.load(model_path)

    def predict(self, features: dict)-> dict:
        df = pd.DataFrame([features])
        # NOTE: preprocessing must match training
        df = pd.get_dummies(df, drop_first=True)
        prob = self.model.predict(df)[0]
        label = "Yes" if prob > 0.5 else "No"
        return {"churn_probability": float(prob), "prediction": label}