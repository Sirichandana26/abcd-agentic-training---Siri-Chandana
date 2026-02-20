import numpy as np

# ---- Cosine Similarity Function ----
def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

# ---- Example Data (Vectors) ----
documents = [
    np.array([1, 2, 3]),
    np.array([2, 3, 4]),
    np.array([10, 10, 10])
]

# ---- Query Vector ----
query = np.array([1, 2, 2])

# ---- Compute Similarities ----
scores = []

for doc in documents:
    score = cosine_similarity(query, doc)
    scores.append(score)

# ---- Display Results ----
for i, score in enumerate(scores):
    print(f"Document {i+1} similarity: {score:.4f}")

# ---- Best Match ----
best_match = np.argmax(scores)
print(f"\nBest Match: Document {best_match+1}")