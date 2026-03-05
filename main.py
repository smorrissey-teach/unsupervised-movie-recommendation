import pandas as pd
from pandasgui import show
import numpy as np
#from tmdb3 import_set_key
import requests
import json
import time

movie = pd.read_csv('movies.csv')
tag = pd.read_csv('tags.csv')
rating = pd.read_csv('ratings.csv')
link =pd.read_csv('links.csv')
genre = pd.read_csv('genre.csv')
movie_genre = pd.read_csv('movie_genre.csv')
# movie_id = pd.merge(
#    movie,
#     link,
#     on='movieId',
#     how='left'
# )
# movie_id.to_csv('player_full.csv', index=False)

#for i in range (2,1186337):
#
# try:
#     with open("movies_data_example.json", "r") as jsonfile:
#         data = json.load(jsonfile)
#     time.sleep(0.5)
#     url = "https://api.themoviedb.org/3/movie/"+str(i)+"?language=en-US"
#
#     headers = {
#     "accept": "application/json",
#     "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJmODhmZmUyOTZlZTE3OGM5NGUzNDAxNTEwOTQ0YjIxMCIsIm5iZiI6MTc3MTI1NDg0NS4zNjQsInN1YiI6IjY5OTMzNDNkNGRlM2E3ZjYyNGZhMzY2ZiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.xo7FytcVInjeW5Xs0TI6rYf3ABgdqjizBHPy8eNPIjg "
#     }
#
#
#     response = requests.get(url, headers=headers)
#
#     print(response.text)
#     data.append(response.text)
#
#     with open("movies_data_example.json", "w") as jsonfile:
#         json.dump(data, jsonfile)
#
# except Exception as e:
#     print(e)
#
#


# url = "https://api.themoviedb.org/3/movie/862?language=en-US"
#
# headers = {
#     "accept": "application/json",
#     "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJmODhmZmUyOTZlZTE3OGM5NGUzNDAxNTEwOTQ0YjIxMCIsIm5iZiI6MTc3MTI1NDg0NS4zNjQsInN1YiI6IjY5OTMzNDNkNGRlM2E3ZjYyNGZhMzY2ZiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.xo7FytcVInjeW5Xs0TI6rYf3ABgdqjizBHPy8eNPIjg "
# }
#
# response = requests.get(url, headers=headers)
#print(response.text)

# Source - https://stackoverflow.com/a/5214587
# Posted by John La Rooy, modified by community. See post 'Timeline' for change history
# Retrieved 2026-02-23, License - CC BY-SA 4.0

#with open("response.json", "w") as text_file:
    #text_file.write(response.text)


# with open('response.json') as f:
#     movies_json = json.load(f)
#     movie = movies_json[0]
#     popularity = movie["popularity"]
#     print(popularity)


#ratings_with_movies = rating.merge(movie, on="movieId")
# ratings_with_movies.to_csv('movie_ratings.csv', index=False)
#hello
#ratings_with_genres = ratings_with_movies.merge(movie_genre, on="movieId")
#ratings_full = ratings_with_genres.merge(genre, on = "genreId")
#ratings_with_genres.to_csv('movie_ratings_with_genres.csv', index=False)

# ratings_with_movies.to_csv('movie_ratings.csv', index=False)
# ratings_full = ratings_with_genres.merge(genre, on="movieID")
ratings_full = pd.read_csv('movie_ratings_with_genres.csv')
user_stats = rating.groupby("userId").agg(
    avg_rating=("rating", "mean"),
    rating_count=("rating", "count")

).reset_index()

print(user_stats.head())

user_genre_avg = rating.full.groupby(["userId", "genre_name"])["rating"].mean().reset_index()
# if genre.contain(genre):
#     genre.add(genre)
print(user_genre_avg.head())


# data = {
#   "rating": [],
#   "genres": []
# }
#
# #load data into a DataFrame object:
# df = pd.DataFrame(data)
#
# print(df)