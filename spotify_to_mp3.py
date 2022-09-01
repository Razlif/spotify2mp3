import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from youtubesearchpython import *
import os
from pytube import YouTube

print("\n----- Welcome! -----\n")
print("To get started please input some details")
path = input("\n1. Please enter the directory path for the playlist folders:")
client_id = input("2. Please enter your spotify PREMIUM client id:")
client_sec = input("3. Please enter your spotify PREMIUM secret key:")
print("\nGreat, thank you.")
user_name = input("Now please enter the user ID you want to fetch playlists for (The download will start automatically):")

auth_manager = SpotifyClientCredentials(client_id, client_sec)
sp = spotipy.Spotify(auth_manager=auth_manager)
playlists = sp.user_playlists(user_name)

print("\n\nStaring download...\n")

def you_tube_downloader(url, path):
    yt = YouTube(url)
    audio_file = yt.streams.filter(only_audio=True).first().download(path)
    base, ext = os.path.splitext(audio_file)
    new_file = base + '.mp3'
    os.rename(audio_file, new_file)
    print("Done")

while playlists:
    for i, playlist in enumerate(playlists['items']):
        print(("PLAY LIST: " + playlist['name']))
        playlist_path = path + "/" + playlist['name']
        playlist_details = sp.playlist_items(playlist['uri'], fields=None, limit=100, offset=0, market=None)
        for i2, playlist_detail in enumerate(playlist_details['items']):
            try:
                artist_var = playlist_detail['track']['artists'][0]['name']
                song_var = playlist_detail['track']['name']
                print("artist: " + artist_var + " song: " + song_var)
                yout_phrase = artist_var + " " + song_var + " official"
                customSearch = CustomSearch(yout_phrase, VideoSortOrder.relevance, limit = 1)
                song_url = customSearch.result()['result'][0]['link']
                print(customSearch.result()['result'][0]['link'])
                you_tube_downloader(song_url, playlist_path)
            except:
                print("could not download: " + artist_var + " song: " + song_var)
    if playlists['next']:
        playlists = sp.next(playlists)
    else:
        playlists = None