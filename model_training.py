import pandas as pd
import numpy as np
import ast
import pickle
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# Load the two CSV files
movies = pd.read_csv("data/tmdb_5000_movies.csv")
credits = pd.read_csv("data/tmdb_5000_credits.csv")

# Merge them on the 'title' column
df = movies.merge(credits, on='title')

# Function to extract the first name from JSON-like strings
def extract_name(text):
    try:
        L = ast.literal_eval(text)
        if isinstance(L, list) and len(L) > 0:
            return L[0]['name']
    except:
        return np.nan

# Extract genre, main actor, and director
df['main_genre'] = df['genres'].apply(extract_name)
df['main_actor'] = df['cast'].apply(extract_name)
df['main_director'] = df['crew'].apply(
    lambda x: next((i['name'] for i in ast.literal_eval(x) if i['job'] == 'Director'), np.nan)
)

# Drop rows with missing values
df.dropna(subset=['budget', 'popularity', 'main_genre', 'main_actor', 'main_director', 'vote_average'], inplace=True)

# Encode categorical features
le_genre = LabelEncoder()
le_actor = LabelEncoder()
le_director = LabelEncoder()

df['main_genre'] = le_genre.fit_transform(df['main_genre'])
df['main_actor'] = le_actor.fit_transform(df['main_actor'])
df['main_director'] = le_director.fit_transform(df['main_director'])

# Features and Target
X = df[['budget', 'popularity', 'main_genre', 'main_actor', 'main_director']]
y = df['vote_average']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

# Model training
model = RandomForestRegressor()
model.fit(X_train, y_train)

# Save the model to a file
with open("model/rating_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Model trained and saved successfully as rating_model.pkl")
