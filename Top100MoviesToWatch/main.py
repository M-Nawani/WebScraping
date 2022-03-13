import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(url=URL)
web_html = response.text

soup = BeautifulSoup(web_html, "html.parser")
movie_titles = soup.find_all(name="h3", class_="title")

titles = [movie_title.getText() for movie_title in reversed(movie_titles)]
with open("movies.txt", "w") as file:
    for title in titles:
        file.write(f"{title}\n")


