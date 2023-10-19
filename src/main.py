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


def search_movie():
    name = movie_entry.get()
    response = request_data(name)
    movie = Movie(
        response["Title"],
        response["Year"],
        response["Rated"],
        response["Plot"],
        response["Director"],
    )
    movie_window = Toplevel()
    movie_window.title(movie.getTitle())
    movie_window.config(padx=10, pady=10)
    movie_window.geometry("1280x720")

    title_label = Label(
        movie_window, text=f"Título: {movie.getTitle()}", justify=CENTER
    )
    title_label.grid(row=2, column=0)

    year_label = Label(
        movie_window, text=f"Ano de lançamento: {movie.getYear()}", justify=CENTER
    )
    year_label.grid(row=4, column=0)

    rating_label = Label(
        movie_window, text=f"Classificação: {movie.getRating()}", justify=CENTER
    )
    rating_label.grid(row=6, column=0)

    plot_label = Label(movie_window, text=f"Sinopse: {movie.getPlot()}", justify=CENTER)
    plot_label.grid(row=8, column=0)

    director_label = Label(
        movie_window, text=f"Diretor(es): {movie.getDirector()}", justify=CENTER
    )
    director_label.grid(row=10, column=0)

    favorite_button = Button(movie_window, text="Favoritar", width=15)
    favorite_button.grid(row=12, column=0, pady=10)

    exit_button = Button(
        movie_window, text="Fechar", width=15, command=movie_window.destroy
    )
    exit_button.grid(row=14, column=0, pady=10)


if __name__ == "__main__":
    window = Tk()
    window.title("OmniMovies")
    window.config(padx=100, pady=100)
    window.geometry("600x400")

    search_label = Label(text="Nome do Filme:")
    search_label.grid(row=2, column=0)

    movie_entry = Entry(width=30)
    movie_entry.grid(row=2, column=1, columnspan=2)
    movie_entry.focus()

    search_button = Button(text="Pesquisar", width=20, command=search_movie)
    search_button.grid(row=4, column=1, pady=10)

    favorite_label = Label(text="Filmes Favoritos:")
    favorite_label.grid(row=80, column=0, pady=20)

    list_favorite_button = Button(text="Listar", width=20)
    list_favorite_button.grid(row=80, column=1, pady=20)

    window.mainloop()
