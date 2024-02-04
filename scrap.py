import requests
import bs4 as bs
import urllib.request

def fetchandsavetofile(url, path):
    r = requests.get(url)
    with open(path, "w", encoding="utf-8") as f:
        f.write(r.text)

url = "https://timesofindia.indiatimes.com/city/delhi"

fetchandsavetofile(url, "webdata/delhi.html")