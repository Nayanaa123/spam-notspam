import pandas as pd
import nltk
import re
import joblib

from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

nltk.download('stopwords')

df = pd.read_csv(
    "dataset/spam.csv",
    encoding='latin-1'
)

df = df[['v1', 'v2']]

df.columns = ['label', 'message']

df['label'] = df['label'].map({
    'ham': 0,
    'spam': 1
})

ps = PorterStemmer()

stop_words = set(stopwords.words('english'))

def clean_text(text):

    text = re.sub('[^a-zA-Z]', ' ', text)

    text = text.lower()

    words = text.split()

    words = [
        ps.stem(word)
        for word in words
        if word not in stop_words
    ]

    return " ".join(words)

df['message'] = df['message'].apply(clean_text)

X = df['message']

y = df['label']

vectorizer = TfidfVectorizer(max_features=5000)

X = vectorizer.fit_transform(X).toarray()

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = MultinomialNB()

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("Accuracy :", accuracy)

joblib.dump(model, 'models/spam_model.pkl')

joblib.dump(vectorizer, 'models/vectorizer.pkl')

print("Model Saved Successfully")