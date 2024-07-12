import requests
from bs4 import BeautifulSoup

date = input("What date would you like to get the top 100 songs from? (YYYY-MM-DD) \n")

response = requests.get(f'https://www.billboard.com/charts/hot-100/{date}/')

soup = BeautifulSoup(response.text, 'html.parser')

song_tags = soup.select(selector="li ul li h3")
songs = [song_tag.getText().strip() for song_tag in song_tags]
print(songs)