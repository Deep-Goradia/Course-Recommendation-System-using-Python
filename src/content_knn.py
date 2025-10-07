from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors
from preprocess import clean_text

class ContentKNN:
    def __init__(self, items, text_col):
        """
        items: DataFrame (courses or materials)
        text_col: column to vectorize (e.g., 'description')
        """
        self.items = items.copy()
        self.items[text_col] = self.items[text_col].apply(clean_text)
        self.vectorizer = TfidfVectorizer(stop_words="english")
        self.vectors = self.vectorizer.fit_transform(self.items[text_col])
        self.knn = NearestNeighbors(metric="cosine")
        self.knn.fit(self.vectors)
        self.text_col = text_col

    def recommend_by_index(self, idx, k=5):
        """Recommend k similar items given an index"""
        distances, indices = self.knn.kneighbors(
            self.vectors[idx], n_neighbors=min(k+1, len(self.items))
        )
        recs = []
        for i in indices.flatten():
            if i != idx:  # skip the selected item itself
                recs.append(self.items.iloc[i])
        return recs
