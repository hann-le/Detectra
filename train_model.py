import os
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
import joblib
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

DATA_PATH = "data/emails.csv"  # Path to the dataset CSV file
MODEL_DIR = "model"            # Directory to save the trained model
MODEL_PATH = os.path.join(MODEL_DIR, "phishing_model.pkl")  # Full path to the saved model

# Step 1: Load dataset
# Check if the dataset file exists before loading
if not os.path.exists(DATA_PATH):
    raise FileNotFoundError(f"Dataset not found at {DATA_PATH}")

# Load the CSV file into a pandas DataFrame
df = pd.read_csv(DATA_PATH)

#  Make sure required columns are present
if "text" not in df.columns or "label" not in df.columns:
    raise ValueError("CSV must contain 'text' and 'label' columns.")

# Step 2: Train/test split for evaluation
# Split the dataset into 80% training and 20% testing
X_train, X_test, y_train, y_test = train_test_split(df["text"], df["label"], test_size=0.2, random_state=42)

# Step 3: Create a pipeline
# This pipeline first converts the text to TF-IDF features, then applies Naive Bayes for classification
model = make_pipeline(TfidfVectorizer(), MultinomialNB())

# Step 4: Train the model
# Fit the model using the training data
model.fit(X_train, y_train)

# Step 5: Evaluate the model
# Predict on the test set
y_pred = model.predict(X_test)

# Print out precision, recall, and F1-score
print("Evaluation on test data:")
print(classification_report(y_test, y_pred))

# Step 6: Save the trained model
# Make sure the model directory exists, then save the model using joblib
os.makedirs(MODEL_DIR, exist_ok=True)
joblib.dump(model, MODEL_PATH)
print(f"✅ Model saved to: {MODEL_PATH}")
