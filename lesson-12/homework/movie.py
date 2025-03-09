import requests
import random

def get_movie(genre, api_key):
    genre_url = "https://api.themoviedb.org/3/genre/movie/list"
    genre_params = {'api_key': api_key, 'language': 'en-US'}
    genre_response = requests.get(genre_url, params=genre_params)

    if genre_response.status_code != 200:
        print("Error fetching genres.")
        return

    genres = genre_response.json().get('genres', [])
    genre_id = next((g['id'] for g in genres if g['name'].lower() == genre.lower()), None)

    if not genre_id:
        print("Genre not found.")
        return

    movie_url = "https://api.themoviedb.org/3/discover/movie"
    movie_params = {
        'api_key': api_key,
        'with_genres': genre_id,
        'language': 'en-US',
        'page': random.randint(1, 5)  
    }

    movie_response = requests.get(movie_url, params=movie_params)

    if movie_response.status_code == 200:
        movies = movie_response.json().get('results', [])
        if movies:
            movie = random.choice(movies)
            print(f" Random {genre.capitalize()} Movie Recommendation:")
            print(f"Title: {movie['title']}")
            print(f"Overview: {movie['overview']}")
        else:
            print("No movies found for this genre.")
    else:
        print("Error fetching movies.")

if __name__ == "__main__":
    api_key = "f70f2beda4e5cf6a7194a83fd10406b8"
    genre = input("Enter a movie genre: ")
    get_movie(genre, api_key)