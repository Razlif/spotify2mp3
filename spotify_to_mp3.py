
##########################
#     Import packages    #
##########################

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from youtubesearchpython import CustomSearch, VideoSortOrder
import os
from pytube import YouTube
import sys
import argparse
from dotenv import load_dotenv, find_dotenv



#########################################
#     Download from youtube Function    #
#########################################

def you_tube_downloader(url, path):
    yt = YouTube(url)
    audio_file = yt.streams.filter(only_audio=True).first().download(path)
    base, ext = os.path.splitext(audio_file)
    new_file = base + '.mp3'
    os.rename(audio_file, new_file)
    print("Done")




############################
#     Getting arguments    #
############################

script_name = sys.argv[0]
parser = argparse.ArgumentParser(description='If you are having problems running the script please go over the README file, make sure you have installed the necessary packages in the requirments.txt file and make sure you have updated the keys.env file with the correct credentials. Command line example: $ python3 spotify_to_mp3.py --path <download path for the mp3 folders> --uname <the spotify user name>')
parser.add_argument("--path", help="The path for the downloaded playlis folders", default='None')
parser.add_argument("--uname", help="The spotify username to download playlists from", default='None')
args = parser.parse_args()
path = args.path
user_name = args.uname
if path == "None":
	print("\n----- Welcome! -----\n")
	print("To get started please input some details")
	path = input("\n1. Please enter the directory path for the downloads:")
	print("\nGreat, thank you.")
	user_name = input("Now please enter the user name you want to fetch playlists for (The download will start automatically):")




##################################
#   Connecting to Spotify api    #
##################################

load_dotenv(find_dotenv())
client_sec = os.environ.get('SPOTIFY_SECRET')
client_id = os.environ.get('SPOTIFY_CLIENT')
auth_manager = SpotifyClientCredentials(client_id, client_sec)
sp = spotipy.Spotify(auth_manager=auth_manager)
playlists = sp.user_playlists(user_name)
print("\n\nStarting download...\n")





####################################################################
#   Locating spotify playlist songs on youtube and saving as mp3   #
####################################################################

while playlists:
    for playlist in playlists['items']:
        print("PLAY LIST: " + playlist['name'])
        playlist_path = path + "/" + user_name + "/" + playlist['name']
        playlist_details = sp.playlist_items(playlist['uri'], fields=None, limit=100, offset=0, market=None)
        for playlist_detail in playlist_details['items']:
            try:
                artist_var = playlist_detail['track']['artists'][0]['name']
                song_var = playlist_detail['track']['name']
                print("artist: " + artist_var + " song: " + song_var)
                yout_phrase = artist_var + " " + song_var + " official"
                custom_search = CustomSearch(yout_phrase, VideoSortOrder.relevance, limit = 1)
                song_url = custom_search.result()['result'][0]['link']
                print(custom_search.result()['result'][0]['link'])
                you_tube_downloader(song_url, playlist_path)
            except:
                print("could not download song")
    if playlists['next']:
        playlists = sp.next(playlists)
    else:
        playlists = None
    print(user_name + " Completed")
