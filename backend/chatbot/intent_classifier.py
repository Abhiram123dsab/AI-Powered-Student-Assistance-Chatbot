import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import joblib

nlp = spacy.load("en_core_web_sm")
vectorizer = joblib.load('vectorizer.joblib')
clf = joblib.load('intent_classifier.joblib')

def classify_intent(message):
    doc = nlp(message.lower())
    vectorized_message = vectorizer.transform([" ".join([token.lemma_ for token in doc])])
    intent = clf.predict(vectorized_message)[0]
    return intent