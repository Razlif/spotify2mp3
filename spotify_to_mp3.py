
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

parser = argparse.ArgumentParser(description='If you are having problems running the script please go over the README file and make sure you have installed the necessary packages in the requirments.txt file. If you are sending arguments through the command line make sure they are correct. Example: $ python3 spotify_to_mp3.py --path <download path for the mp3 folders> --id <spotify client id> --key <spotify secret key> --uname <the spotify user name>')
parser.add_argument("--path", help="The path for the downloaded playlis folders", default='None')
parser.add_argument("--id", help="The spotify client id ", default='None')
parser.add_argument("--key", help="The spotify app secert key", default='None')
parser.add_argument("--uname", help="The spotify username to download playlists from", default='None')
args = parser.parse_args()
script_name = sys.argv[0]
path = args.path
client_id = args.id
client_sec = args.key
user_name = args.uname
if path=="None":
	print("\n----- Welcome! -----\n")
	print("To get started please input some details")
	path = input("\n1. Please enter the directory path for the playlist folders:")
	client_id = input("2. Please enter your spotify PREMIUM client id:")
	client_sec = input("3. Please enter your spotify PREMIUM secret key:")
	print("\nGreat, thank you.")
	user_name = input("Now please enter the user ID you want to fetch playlists for (The download will start automatically):")




##################################
#   Connecting to Spotify api    #
##################################

auth_manager = SpotifyClientCredentials(client_id, client_sec)
sp = spotipy.Spotify(auth_manager=auth_manager)
playlists = sp.user_playlists(user_name)
print("\n\nStaring download...\n")





####################################################################
#   Locating spotify playlist songs on youtube and saving as mp3   #
####################################################################

while playlists:
    for i, playlist in enumerate(playlists['items']):
        print("PLAY LIST: " + playlist['name'])
        playlist_path = path + "/" + playlist['name']
        playlist_details = sp.playlist_items(playlist['uri'], fields=None, limit=100, offset=0, market=None)
        for ii, playlist_detail in enumerate(playlist_details['items']):
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
