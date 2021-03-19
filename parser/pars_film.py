import requests
from bs4 import BeautifulSoup
import random

with open('ind.html', encoding='utf-8') as file:
    src = file.read()

soup = BeautifulSoup(src, 'lxml')

als_film = soup.find_all(class_='titleColumn')
#als_rating = soup.find_all(class_='ratingColumn imdbRating')

film_name = []

for item in als_film:
    item_text = item.get_text(strip=True)
    film_name.append(item_text)
    # item_href = item.get("href")



"""teg_film = soup.find(class_='titleColumn')
a = str(teg_film.text)
print(a[16:50].rstrip())
print('1')"""
"""for item in teg_film:
    nm_film = item.find_all('td')

    tt = nm_film[0].find("a").text
    print(tt)"""


als_rating = soup.find_all(class_='ratingColumn imdbRating')
film_rait = []
for item in als_rating:
    item_rait= item.get_text(strip=True)
    film_rait.append(item_rait)


x = random.randint(0,249)
if x < 10:
    print(film_name[x][2:], film_rait[x] + ' IMDb')
elif x > 10 and x < 100:
    print(film_name[x][3:], film_rait[x] + ' IMDb')
else:
    print(film_name[x][4:], film_rait[x] + ' IMDb')

