import joblib

def load_production_model():
    model = joblib.load("models/production_model.pkl")
    return model