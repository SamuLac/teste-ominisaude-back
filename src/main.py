import requests


def request_data(name):
    request = requests.get(
        f"http://www.omdbapi.com/?i=tt3896198&apikey=e588ec9f&t={name}"
    )

    return request.content


response = request_data("avatar")
print(response)
