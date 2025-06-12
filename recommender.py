import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.neighbors import NearestNeighbors

class MovieRecommender:
    def __init__(self, csv_path="data/movies.csv"):
        self.df = pd.read_csv(csv_path)
        self.encoder = OneHotEncoder()
        self.model = NearestNeighbors(n_neighbors=10, metric='hamming')
        self._prepare_model()

    def _prepare_model(self):
        features = self.df[['Genre', 'Language', 'Theme']]
        self.encoded_features = self.encoder.fit_transform(features).toarray()
        self.model.fit(self.encoded_features)

    def recommend(self, Genre, Language, Theme, top_k=3):
        # Step 1: Strictly filter the dataset
        filtered_df = self.df[
            (self.df['Genre'].str.lower() == Genre.lower()) &
            (self.df['Language'].str.lower() == Language.lower()) &
            (self.df['Theme'].str.lower() == Theme.lower())
        ]

        # Step 2: If matches found, return top_k from filtered list
        if not filtered_df.empty:
            return filtered_df['Movie Name'].head(top_k).tolist()

        # Step 3 (Optional fallback): If no strict matches found, use Nearest Neighbors
        user_input = [[Genre, Language, Theme]]
        user_encoded = self.encoder.transform(user_input).toarray()
        distances, indices = self.model.kneighbors(user_encoded, n_neighbors=top_k)
        return self.df.iloc[indices[0]]['Movie Name'].tolist()
