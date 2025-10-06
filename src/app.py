from fastapi import FastAPI
from pydantic import BaseModel
from src.predict import Predictor

app = FastAPI(title = "Telco churn prediction API service")
predictor = Predictor()

class CustomerData(BaseModel):
    AvgMonthlyLongDistanceCharges: float
    population: float
    AvgMonthlyGBDownload: float
    # Add all necessary features here

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/predict")
def predict_churn(data: dict):
    result = predictor.predict(data)
    return result