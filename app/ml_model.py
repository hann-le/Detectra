import joblib
import os

# Load the trained model
model_path = os.path.join("model", "phishing_model.pkl")
model = joblib.load(model_path)

def predict_email(text):
    """
    Predict using the trained ML model.
    Returns 1 for phishing, 0 for safe.
    """
    prediction = model.predict([text])[0]
    return prediction

#  fallback dummy rule-based predictor
def predict_phishing(text):
    """
    Basic rule-based prediction (used for backup/testing only).
    """
    if "login" in text.lower() and "verify" in text.lower():
        return 1  # phishing
    return 0  # safe
