# tmdb_app.py

from static_movies import HINDI_MOVIES, ENGLISH_MOVIES, BENGALI_MOVIES

def get_movie_data_by_language(language):
    """
    Returns a list of movie dictionaries for the given language.
    Supported values: "Hindi", "English", "Bengali"
    """
    if language == "Hindi":
        return HINDI_MOVIES
    elif language == "English":
        return ENGLISH_MOVIES
    elif language == "Bengali":
        return BENGALI_MOVIES
    else:
        return []

def get_movie_by_title(language, title):
    """
    Returns the full details of a selected movie by its title.
    """
    movie_list = get_movie_data_by_language(language)
    for movie in movie_list:
        if movie["title"].lower() == title.lower():
            return movie
    return None

def extract_movie_features(movie):
    """
    Converts movie dictionary to model input format.
    Returns: budget, popularity, genre_code, actor_code, director_code
    """
    budget = movie.get("budget", 0)
    popularity = movie.get("popularity", 10.0)

    # Use hash-based codes (bounded to match training scale)
    genre_code = abs(hash(movie.get("genre", ""))) % 21
    actor_code = abs(hash(movie.get("actor", ""))) % 201
    director_code = abs(hash(movie.get("director", ""))) % 101

    return [budget, popularity, genre_code, actor_code, director_code]
