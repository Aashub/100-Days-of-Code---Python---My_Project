from bs4 import BeautifulSoup
import requests


# requesting a url
response = requests.get(url="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")

movies_webpage = response.text

# creating object for webscrapping from the class
soup = BeautifulSoup(movies_webpage, "html.parser")

# scrapping the movie title data
movie_title = soup.find_all(name="h3", class_ = "title")

movie_list = []
# this for loop will create a list of top 100 movies of all time
for movie in movie_title:
    try:
        movie_list.append(movie.text.split(")")[1])
    except IndexError:
        movie_list.append(movie.text.split(":")[1])


num = 99
# here we are creating a txt file for top 100 movies of all time.
with open(file="top_100_movies.txt", mode="w",  encoding="utf-8") as file:

    for movie in reversed(movie_list):
        file.write(f"{len(movie_list) - num}){movie}\n")

        num -= 1



