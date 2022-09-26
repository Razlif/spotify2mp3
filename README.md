# Introduction

This project is intended to help you download spotify user playlists as mp3 files.

The song names are exatrcted using the spotify api and then loacted and downloaded from youtube as mp3 files.

* To run this project you will need to have a paid spotify account in order to get your the client id and api key.


# Installation

First clone the project
```
git clone https://github.com/Razlif/spotify2mp3.git
```
Next install the required packages
```
pip3 install --user -r requirements.txt
```

# Spotify Credentials

To use the program you will need your spotify client id and your spotify secret key to be able to access the spotify api.

To get them, follow these steps:

Go to the [spotify developer section](https://developer.spotify.com/dashboard/applications)

1. Log into your Spotify account.

2. Click on ‘Create an app’.

3. Enter an ‘App name’ and an ‘App description’ and mark the checkboxes.

4. After the app is created you will see your ‘Client Id’. Then can click on ‘Show client secret` to reveal your ’Client secret key’.

* The spotify user name can be located in the the url for the user's main page for example, https://open.spotify.com/user/< user >


# Setting up enviroment variables

Next edit the .env file in the project folder and include the spotify credentials.
.env
```
SPOTIFY_SECRET = "Your spotify secret key"
SPOTIFY_CLIENT = "Your spotify client ID"
```

# Running the script on a single user

Now you can run the python script directly from the command line
```
python3 spotify_to_mp3.py
```
This will prompt you to enter the download path and the spotify username that has the playlists to download.

you can also input the arguments directly in the command line:
```
python3 spotify_to_mp3.py --path <download path for the mp3 folders> --uname <the spotify user name>
```

# Running the script on multiple users

You can also run the script on multiple users at one time.

Simply update the users.txt file with a list of users to download from.
>make sure to add each user name in a new line
users.txt
```
ExampleUser1
ExampleUser2
...
```

next mark the main.sh file as executable and run it from the command line:
>Make sure to include the main download path as the first positional argument
```
$ chmod +x main.sh
$ ./main.sh <main download path>
```

# Have Fun!
