from bs4 import BeautifulSoup

with open('ind3.html', encoding='utf-8') as file:
    src = file.read()

soup = BeautifulSoup(src, 'lxml')

als_film_poisk = soup.find_all(class_='selection-film-item-meta__name')

film_name_poisk3 = []

for item in als_film_poisk:
    item_text = item.get_text()
    film_name_poisk3.append(item_text)


als_film_poisk2 = soup.find_all(class_='rating__value rating__value_positive')

film_rait_poisk3 = []

for item in als_film_poisk2:
    item_text = item.get_text()
    film_rait_poisk3.append(item_text)