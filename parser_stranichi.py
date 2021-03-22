import requests

url = "https://www.imdb.com/chart/top/"
headers = {
    'accept': '*/*',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4437.0 Safari/537.36 Edg/91.0.831.0'
}
req = requests.get(url, headers=headers)

src = req.text

with open("ind.html", "w", encoding='utf-8') as file:
    file.write(src)
