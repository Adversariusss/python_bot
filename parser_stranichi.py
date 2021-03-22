import requests

url = "https://www.imdb.com/chart/top/"
headers = {
    'accept': '*/*',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.54'
}
req = requests.get(url, headers=headers)

src = req.text

with open("ind.html", "w", encoding='utf-8') as file:
    file.write(src)
