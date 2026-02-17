import pandas as pd
import numpy as np
#from tmdb3 import_set_key
import requests
import json
import time

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

for i in range (2,1186337):
    try:
        with open("movies.json", "r") as jsonfile:
            data = json.load(jsonfile)
        time.sleep(0.5)
        url = "https://api.themoviedb.org/3/movie/"+str(i)+"?language=en-US"

        headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJmODhmZmUyOTZlZTE3OGM5NGUzNDAxNTEwOTQ0YjIxMCIsIm5iZiI6MTc3MTI1NDg0NS4zNjQsInN1YiI6IjY5OTMzNDNkNGRlM2E3ZjYyNGZhMzY2ZiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.xo7FytcVInjeW5Xs0TI6rYf3ABgdqjizBHPy8eNPIjg "
        }


        response = requests.get(url, headers=headers)

        print(response.text)
        data.append(response.text)

        with open("movies.json", "w") as jsonfile:
            json.dump(data, jsonfile)

    except Exception as e:
        print(e)