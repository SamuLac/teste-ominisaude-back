import requests
import json
from tkinter import *
from classes.movie import Movie


def request_data(name):
    request = requests.get(
        f"http://www.omdbapi.com/?i=tt3896198&apikey=e588ec9f&t={name}"
    )
    data = json.loads(request.content)
    return data


response = request_data("avatar")
movie = Movie(
    response["Title"],
    response["Year"],
    response["Rated"],
    response["Plot"],
    response["Director"],
)
# print(
#   movie.getTitle(),
#   movie.getYear(),
#    movie.getRating(),
#    movie.getPlot(),
#    movie.getDirector(),
#)

if __name__ == '__main__':
  window = Tk()
  window.title("OmniMovies")
  window.config(padx=100, pady=100)
  window.geometry("600x400")

  search_label = Label(text="Nome do Filme:")
  search_label.grid(row=2, column=0)

  movie_entry = Entry(width=30)
  movie_entry.grid(row=2, column=1, columnspan=2)
  movie_entry.focus() 

  search_button = Button(text="Pesquisar", width=20)
  search_button.grid(row=4, column= 1, pady= 10)

  favorite_label = Label(text="Filmes Favoritos:")
  favorite_label.grid(row=80, column=0, pady= 20)
  
  favorite_button = Button(text="Listar", width=20)
  favorite_button.grid(row=80, column=1, pady= 20)
  
  window.mainloop()