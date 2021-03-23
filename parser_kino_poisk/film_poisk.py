import sys
sys.path.append('D:\\ммма\\Pycharm_Project\\python_bot')
from prs_film import film_name_poisk, film_rait_poisk
from prs2 import film_name_poisk2, film_rait_poisk2
from pars3 import film_name_poisk3, film_rait_poisk3
from pars4 import film_name_poisk4, film_rait_poisk4
from pars5 import film_name_poisk5, film_rait_poisk5

all_film_poisk = []
all_film_rait_poisk = []

# Добавление всех названий фильмов в 1 переменную с 5 спарсенных страниц
for i in film_name_poisk:
    all_film_poisk.append(i)

for i in film_name_poisk2:
    all_film_poisk.append(i)

for i in film_name_poisk3:
    all_film_poisk.append(i)

for i in film_name_poisk4:
    all_film_poisk.append(i)

for i in film_name_poisk5:
    all_film_poisk.append(i)

# Добавление рейтинга фильмов в 1 переменную с 5 спарсенных страниц
for i in film_rait_poisk:
    all_film_rait_poisk.append(i)

for i in film_rait_poisk2:
    all_film_rait_poisk.append(i)

for i in film_rait_poisk3:
    all_film_rait_poisk.append(i)

for i in film_rait_poisk4:
    all_film_rait_poisk.append(i)

for i in film_rait_poisk5:
    all_film_rait_poisk.append(i)


