import requests
from bs4 import BeautifulSoup
import csv


url = "https://www.imdb.com/chart/top/"
R = requests.get(url)
soup = BeautifulSoup(R.text, "html.parser")
movies = soup.find("tbody", {"class": "lister-list"}).find_all("tr")
header = ["Name", "Date", "IMDB Rating"]
info = []
for movie in movies:
    name = movie.find("td", {"class": "titleColumn"}).a.text
    date = movie.find("span", {"class": "secondaryInfo"}).text.strip("()")
    imdb_rating = movie.find("td", {"class": "ratingColumn imdbRating"}).strong.text
    info.append([name, date, imdb_rating])

with open('imdb250.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(info)

