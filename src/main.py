import requests
import json
from tkinter import messagebox, Tk, Label, Entry, Button, Toplevel, Listbox, END
from classes.movie import Movie


def request_data(name):
    request = requests.get(
        f"http://www.omdbapi.com/?i=tt3896198&apikey=e588ec9f&t={name}"
    )
    data = json.loads(request.content)
    return data

def list_favorite():
    favorite_window = Toplevel()
    favorite_window.title("Lista de Favoritos")
    favorite_window.config(padx=10, pady=10)
    favorite_window.geometry("600x400")

    json_file = open("favorites.json", "r")
    favorite_list = json.load(json_file)
    json_file.close()
    print(len(favorite_list['Movies']))
    list_box = Listbox(favorite_window,height=len(favorite_list['Movies']))
    list_box.grid(row=0,column=0)

    for favorite in favorite_list["Movies"]:
        list_box.insert(END,favorite.get("Title"))

def add_favorite(movie):
    if messagebox.askyesno("Favoritar", "Deseja mesmo favoritar esse filme?"):
        json_file = open("favorites.json", "r")
        favorite_list = json.load(json_file)
        json_file.close()
        if len(favorite_list["Movies"]) == 0:
            favorite_list["Movies"].append(
                {
                    "Title": movie.getTitle(),
                    "Year": movie.getYear(),
                    "Rated": movie.getRating(),
                    "Plot": movie.getPlot(),
                    "Director": movie.getDirector(),
                }
            )
            json_file = open("favorites.json", "w")
            json.dump(favorite_list, json_file)
            json_file.close()
            messagebox.showinfo("Sucesso", "O filme foi adicionado com sucesso")
        else:
            itsFavorite = False
            for i in range(len(favorite_list["Movies"])):
                if favorite_list["Movies"][i].get("Title") == movie.getTitle():
                    messagebox.showerror("Erro!", "Esse filme já é favorito")
                    itsFavorite = True

            if not itsFavorite:
                favorite_list["Movies"].append(
                    {
                        "Title": movie.getTitle(),
                        "Year": movie.getYear(),
                        "Rated": movie.getRating(),
                        "Plot": movie.getPlot(),
                        "Director": movie.getDirector(),
                    }
                )
                json_file = open("favorites.json", "w")
                json.dump(favorite_list, json_file)
                json_file.close()
                messagebox.showinfo("Sucesso", "O filme foi adicionado com sucesso")


def search_movie():
    name = movie_entry.get()
    if len(name) == 0:
        messagebox.showerror("Erro!", "Por favor insira um título válido")
    else:
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

        title_label = Label(movie_window, text=f"Título: {movie.getTitle()}")
        title_label.grid(row=2, column=0)

        year_label = Label(movie_window, text=f"Ano de lançamento: {movie.getYear()}")
        year_label.grid(row=4, column=0)

        rating_label = Label(movie_window, text=f"Classificação: {movie.getRating()}")
        rating_label.grid(row=6, column=0)

        plot_label = Label(movie_window, text=f"Sinopse: {movie.getPlot()}")
        plot_label.grid(row=8, column=0)

        director_label = Label(movie_window, text=f"Diretor(es): {movie.getDirector()}")
        director_label.grid(row=10, column=0)

        favorite_button = Button(
            movie_window,
            text="Favoritar",
            width=15,
            command=lambda: add_favorite(movie),
        )
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

    list_favorite_button = Button(text="Listar", width=20, command=list_favorite)
    list_favorite_button.grid(row=80, column=1, pady=20)

    window.mainloop()
