import pickle
import re
import nltk

nltk.download('stopwords')
from nltk.corpus import stopwords

# Load trained model and vectorizer
model = pickle.load(open("sentiment_model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

stop_words = set(stopwords.words('english')) - {"not", "no"}

def clean_text(text):
    text = str(text).lower()
    text = re.sub(r'[^a-z\s]', '', text)
    words = text.split()
    return " ".join(w for w in words if w not in stop_words)

print("===================================")
print(" Sentiment Analysis Model Ready ")
print(" Type 'exit' to stop testing ")
print("===================================")

while True:
    review = input("\nEnter review: ")

    if review.lower() == "exit":
        break

    cleaned = clean_text(review)
    vector = vectorizer.transform([cleaned])
    prediction = model.predict(vector)[0]

    print("Predicted Sentiment:", prediction)
