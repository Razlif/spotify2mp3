# Introduction

This project is intended to help you download spotify user playlists as mp3 files.
The song names are exatrcted using the spotify api and then loacted and downloaded from youtube as mp3 files.

* To run this project you will need to have a paid spotify account

# Installation

First clone the project
```
git clone https://github.com/Razlif/spotify2mp3.git
```
Next install the required packages
```
pip3 install --user -r requirements.txt
```
# Spotify Auth

To use the program you will need your spotify client id and your spotify secret key to be able to access the spotify api.

To get them, follow these steps:

Browse to https://developer.spotify.com/dashboard/applications.

1.Log in with your Spotify account.

2.Click on ‘Create an app’.

3.Pick an ‘App name’ and ‘App description’ of your choice and mark the checkboxes.

4.After creation, you see your ‘Client Id’ and you can click on ‘Show client secret` to unhide your ’Client secret’.

* The spotify user name can be located in the the url for the user's main page for example, https://open.spotify.com/user/<user name>

# Run
There are 2 ways to run the program. If you do
```
python3 spotify_to_mp3.py
```
This will start an interactive version of the script that will prompt you to enter the download path, your client id, your client secret key and finally the spotify username that has the playlists to download.

you can also run the program using command line arguments like so
```
python3 spotify_to_mp3.py --path <download path for the mp3 folders> --id  <spotify client id> --key  <spotify secret key> --uname <the spotify user name>
```

