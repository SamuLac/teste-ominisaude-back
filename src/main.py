import requests
import json
from classes.movie import Movie


def request_data(name):
    request = requests.get(
        f"http://www.omdbapi.com/?i=tt3896198&apikey=e588ec9f&t={name}"
    )
    data = json.loads(request.content)
    return data


response = request_data("avatar")
movie = Movie(response['Title'], response['Year'], response['Rated'], response['Plot'], response['Director'])
print(movie.getTitle(), movie.getYear(), movie.getRating(), movie.getPlot(), movie.getDirector())
