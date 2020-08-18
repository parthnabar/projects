import requests
from bs4 import BeautifulSoup

r1 = requests.get("https://news.google.com/")
coverpage = r1.content
soup1 = BeautifulSoup(coverpage, 'html.parser')
coverpage_news = soup1.find_all('h3', class_="ipQwMb ekueJc RD0gLb")
print(coverpage_news)

print(coverpage_news[4]['href'])
