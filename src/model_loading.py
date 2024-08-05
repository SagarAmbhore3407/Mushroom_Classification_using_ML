
import joblib

def load_model_and_encoders():
    model = joblib.load('models/mushroom_classifier.pkl')
    encoders = joblib.load('models/encoders.pkl')
    return model, encoders
