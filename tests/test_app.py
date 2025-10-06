from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_predict():
    sample_data = {
        "gender": "Male",
        "seniorCitizen": 19,
        "Contract": "Month-to-month"
    }
    response = client.post("/predict", json=sample_data)
    assert response.status_code == 200
    assert "probability" in response.json() and "label" in response.json()
    