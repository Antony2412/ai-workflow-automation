import pickle
from pathlib import Path

# Resolve paths safely
BASE_DIR = Path(__file__).resolve().parents[2]
MODEL_DIR = BASE_DIR / "app" / "ml"

# Load trained artifacts once (on startup)
with open(MODEL_DIR / "model.pkl", "rb") as f:
    model = pickle.load(f)

with open(MODEL_DIR / "vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)


def classify_ticket(text: str) -> str:
    """
    Classify incoming ticket text into a category.
    """
    vector = vectorizer.transform([text])
    prediction = model.predict(vector)
    return prediction[0]
