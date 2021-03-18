import requests
from bs4 import BeautifulSoup
import re


with open('ind.html', encoding='utf-8') as file:
    src = file.read()

soup = BeautifulSoup(src, 'lxml')

als_film = soup.find_all(class_='titleColumn')

film = []

for item in als_film:
    item_text = item.get_text(strip=True)
    #film.append(item_text)
    #item_href = item.get("href")
    print(item_text)

"""teg_film = soup.find(class_='titleColumn')
a = str(teg_film.text)
print(a[16:50].rstrip())
print('1')"""
"""for item in teg_film:
    nm_film = item.find_all('td')

    tt = nm_film[0].find("a").text
    print(tt)"""

'''
als_rating = soup.find_all(class_='ratingColumn imdbRating')

for item in als_rating:
    item_txt = item.text
    print(item_txt)

#ratingColumn imdbRating
'''