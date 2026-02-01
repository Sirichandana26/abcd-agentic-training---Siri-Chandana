import pandas as pd
import re
import nltk
import pickle

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

nltk.download('stopwords')
from nltk.corpus import stopwords

# Load dataset (CSV or Excel)
data = pd.read_excel("dataset.xlsx")  # or read_excel

# Keep only binary labels
data = data[data['sentiment'].isin(['positive', 'negative'])]

stop_words = set(stopwords.words('english')) - {"not", "no"}

def clean_text(text):
    text = str(text).lower()
    text = re.sub(r'[^a-z\s]', '', text)
    return " ".join(
        w for w in text.split() if w not in stop_words
    )

data["clean_review"] = data["review"].apply(clean_text)

vectorizer = TfidfVectorizer(
    max_features=5000,
    min_df=5,
    max_df=0.9,
    ngram_range=(1, 2)
)

X = vectorizer.fit_transform(data["clean_review"])
y = data["sentiment"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))

pickle.dump(model, open("sentiment_model.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))
