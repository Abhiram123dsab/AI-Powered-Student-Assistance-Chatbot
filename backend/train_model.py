import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import joblib

nlp = spacy.load("en_core_web_sm")

def train_intent_classifier():
    # Example training data
    X = [
        "How do I apply for admission?",
        "What are the fees for engineering courses?",
        "Are there any scholarships available?",
    ]
    y = ["admission", "fee", "scholarship"]

    vectorizer = TfidfVectorizer(tokenizer=lambda x: [token.lemma_ for token in nlp(x)])
    X_vectorized = vectorizer.fit_transform(X)

    clf = MultinomialNB()
    clf.fit(X_vectorized, y)

    joblib.dump(vectorizer, 'vectorizer.joblib')
    joblib.dump(clf, 'intent_classifier.joblib')

if __name__ == "__main__":
    train_intent_classifier()
    print("Intent classifier model trained and saved successfully.")