import os
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib

# Paths
PHISHING_PATH = "verified_online.csv"
SAFE_PATH = "data/safe_urls.csv"
MODEL_DIR = "model"
MODEL_PATH = os.path.join(MODEL_DIR, "combined_phishtank_model.pkl")

# Load datasets
phish_df = pd.read_csv(PHISHING_PATH)
safe_df = pd.read_csv(SAFE_PATH)

# Add label columns
phish_df['label'] = 1
safe_df['label'] = 0

# Keep only the url and label columns to simplify
phish_df = phish_df[['url', 'label']]
safe_df = safe_df[['url', 'label']]

# Combine datasets
combined_df = pd.concat([phish_df, safe_df], ignore_index=True)

# Shuffle data
combined_df = combined_df.sample(frac=1, random_state=42).reset_index(drop=True)

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    combined_df['url'], combined_df['label'], test_size=0.2, random_state=42)

# Create model pipeline
model = make_pipeline(TfidfVectorizer(), MultinomialNB())

# Train
model.fit(X_train, y_train)

# Predict and evaluate
y_pred = model.predict(X_test)
print("Classification report:")
print(classification_report(y_test, y_pred))

# Save the model
os.makedirs(MODEL_DIR, exist_ok=True)
joblib.dump(model, MODEL_PATH)
print(f"✅ Model saved to {MODEL_PATH}")

