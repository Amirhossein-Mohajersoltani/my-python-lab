import requests
from bs4 import BeautifulSoup

date = input("what year you would like to travel to? (in YYYY-MM-DD format.)\n")

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}/", headers=headers)
html_doc = response.text


soup = BeautifulSoup(html_doc, "html.parser")

song_elements = soup.select(selector="div.o-chart-results-list-row-container .c-title")

song_titles = [element.getText().strip() for element in song_elements[::4]]

print(song_titles)
print(len(song_titles))


# Spotify

import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID = "71955eb4144c4d1bafdd58abc24b0e28"
CLIENT_SECRET = "1c14a8d35d5f49149bd68de550ed35c9"
REDIRECT_URI = "http://example.com"
SCOPE = "playlist-modify-private"
USER_ID = "oz7f98f7169s8eb3tewntypc9"
authenticate = SpotifyOAuth(client_id=CLIENT_ID,client_secret=CLIENT_SECRET,scope=SCOPE,redirect_uri=REDIRECT_URI)

sp = spotipy.Spotify(auth_manager=authenticate)

sp.user_playlist_create(user=USER_ID, name="Amirs",public=False)