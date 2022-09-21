import requests
from bs4 import BeautifulSoup


url = "https://www.imdb.com/chart/top/"
R = requests.get(url)
soup = BeautifulSoup(R.text, "html.parser")
movies = soup.find("tbody", {"class": "lister-list"}).find_all("tr")

for movie in movies:
    name = movie.find("td", {"class": "titleColumn"}).a.text
    date = movie.find("span", {"class": "secondaryInfo"}).text.strip("()")
    imdb_rating = movie.find("td", {"class": "ratingColumn imdbRating"}).strong.text
    print(name, date, imdb_rating)
