import pandas as pd
import pickle
from pathlib import Path

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Paths
BASE_DIR = Path(__file__).resolve().parents[2]
DATA_PATH = BASE_DIR / "data" / "tickets.csv"
MODEL_DIR = BASE_DIR / "app" / "ml"

# Load data
df = pd.read_csv(DATA_PATH)

X = df["text"]
y = df["category"]

# Vectorization
vectorizer = TfidfVectorizer(
    stop_words="english",
    ngram_range=(1, 2)
)
X_vec = vectorizer.fit_transform(X)

# Train model
model = LogisticRegression(max_iter=1000)
model.fit(X_vec, y)

# Save artifacts
with open(MODEL_DIR / "model.pkl", "wb") as f:
    pickle.dump(model, f)

with open(MODEL_DIR / "vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)

print("✅ Model trained and saved successfully")