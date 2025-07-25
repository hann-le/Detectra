import pandas as pd
import joblib
from sklearn.metrics import classification_report

df_test = pd.read_csv('data/test_500_emails.csv')

X_test = df['url'].tolist()
y_test = df['verified'].map({'yes': 1, 'no': 0})

print("Label distribution in test set:")
print(y_test.value_counts())

model = joblib.load('model/phishing_model.pkl')

y_pred = model.predict(X_test)

print(classification_report(y_test, y_pred))
