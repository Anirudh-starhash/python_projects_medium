from bs4 import BeautifulSoup
import requests
import os

date=input("Enter the date on which you want tp travel back in YYYY-MM-DD format\n")

response=requests.get("https://www.billboard.com/charts/india-songs-hotw/"+date)

soup=BeautifulSoup(response.text,"html.parser")

song_names=soup.select("li ul li h3")
song_names=[song_name.getText().strip() for song_name in song_names]
print(song_names)

client_id=os.environ.get("SPOTIFY_billboard_client_id")
client_secret=os.environ.get("SPOTIFY_billboard_client_secret")

import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="https://example.com",
        client_id=client_id,
        client_secret=client_secret,
        show_dialog=True,
        cache_path="token.txt",
        username="Anirudhpabbaraju", 
    )
)
user_id = sp.current_user()["id"]
print(user_id)

song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    # print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")
        
        
# print(song_uris)

playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
# print(playlist)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)