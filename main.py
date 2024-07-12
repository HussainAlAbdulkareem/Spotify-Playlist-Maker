import requests
from bs4 import BeautifulSoup
import spotipy
from dotenv import load_dotenv
import os

load_dotenv()
date = input("What date would you like to get the top 100 songs from? (YYYY-MM-DD) \n")

response = requests.get(f'https://www.billboard.com/charts/hot-100/{date}/')

soup = BeautifulSoup(response.text, 'html.parser')

song_tags = soup.select(selector="li ul li h3")
songs = [song_tag.getText().strip() for song_tag in song_tags]
print(songs)


auth = spotipy.oauth2.SpotifyOAuth(client_id=os.getenv("CLIENT_ID"), client_secret=os.getenv("CLIENT_SECRET"), redirect_uri="http://example.com")
token = auth.get_access_token()["access_token"]

sp = spotipy.Spotify(auth=token)
user_name = sp.current_user()
