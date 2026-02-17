import pandas as pd
import numpy as np
#from tmdb3 import_set_key
import requests
#set_key('')

movie = pd.read_csv('file/movies.csv')
tag = pd.read_csv('file/tags.csv')
rating = pd.read_csv('file/ratings.csv')
link =pd.read_csv('file/links.csv')

movie_id = pd.merge(
   movie,
    link,
    on='movieId',
    how='left'
)
movie_id.to_csv('player_full.csv', index=False)


url = "https://api.themoviedb.org/3/movie/862?language=en-US"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJmODhmZmUyOTZlZTE3OGM5NGUzNDAxNTEwOTQ0YjIxMCIsIm5iZiI6MTc3MTI1NDg0NS4zNjQsInN1YiI6IjY5OTMzNDNkNGRlM2E3ZjYyNGZhMzY2ZiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.xo7FytcVInjeW5Xs0TI6rYf3ABgdqjizBHPy8eNPIjg "
}


response = requests.get(url, headers=headers)

print(response.text)
movie.json = response.text
