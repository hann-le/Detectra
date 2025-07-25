import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report, accuracy_score

def main():
    train_df = pd.read_parquet('archive/training.parquet')
    test_df = pd.read_parquet('archive/testing.parquet')

    train_df['label'] = train_df['status'].apply(lambda x: 1 if x == 'phishing' else 0)
    test_df['label'] = test_df['status'].apply(lambda x: 1 if x == 'phishing' else 0)

    vectorizer = TfidfVectorizer()
    X_train = vectorizer.fit_transform(train_df['url'])
    X_test = vectorizer.transform(test_df['url'])

    y_train = train_df['label']
    y_test = test_df['label']

    model = MultinomialNB()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    print("Accuracy:", accuracy_score(y_test, y_pred))
    print(classification_report(y_test, y_pred))

if __name__ == "__main__":
    main()

