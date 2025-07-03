import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
import dotenv

dotenv.load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
REDIRECT_URI = os.getenv("REDIRECT_URI")
SCOPE = os.getenv("SCOPE")
USER_ID = os.getenv("USER_ID")
NAME = os.getenv("NAME")

ACCEPT_LANGUAGE = os.getenv("ACCEPT_LANGUAGE")
USER_AGENT = os.getenv("USER_AGENT")

date = input("what year you would like to travel to? (in YYYY-MM-DD format.)\n")

headers = {
    "User-Agent": USER_AGENT,
    "Accept-Language": ACCEPT_LANGUAGE
}

response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}/", headers=headers)
html_doc = response.text


soup = BeautifulSoup(html_doc, "html.parser")

song_elements = soup.select(selector="div.o-chart-results-list-row-container .c-title")

song_titles = [element.getText().strip() for element in song_elements[::4]]

print(song_titles)
print(len(song_titles))


# Spotify




authenticate = SpotifyOAuth(client_id=CLIENT_ID,client_secret=CLIENT_SECRET,scope=SCOPE,redirect_uri=REDIRECT_URI)

sp = spotipy.Spotify(auth_manager=authenticate)

sp.user_playlist_create(user=USER_ID, name=NAME,public=False)