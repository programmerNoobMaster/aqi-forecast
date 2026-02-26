from fastapi import FastAPI
import pandas as pd
from src.model_training.load_production_model import load_production_model

app = FastAPI()

model = load_production_model()


@app.get("/")
def home():
    return {"message": "AQI Prediction API is running"}


@app.post("/predict")
def predict(data: dict):

    df = pd.DataFrame([data])

    prediction = model.predict(df)

    return {"predicted_PM2.5": float(prediction[0])}