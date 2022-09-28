#!/bin/bash
path=$1
echo $path
input="~/spotify2mp3/users.txt"
while read -r line
do
  user=$line
  echo $user
  python3 spotify_to_mp3.py --path $path --uname $user
done < "$input"
