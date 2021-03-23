import requests

url = "https://www.kinopoisk.ru/lists/top250/?page=5"
headers = {
    'accept': '*/*',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'
}
req = requests.get(url, headers=headers)

src1 = req.text
print(src1)
with open("ind5.html", "w", encoding='utf-8') as file:
    file.write(src1)
    print("end")

