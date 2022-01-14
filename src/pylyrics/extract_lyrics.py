# Authors: Abhiket Gaurav, Artan Zandian, Macy Chan, Manju Abhinandana Kumar
# Date: 2022-01-14

import requests
import os, sys
import pandas as pd
import json
import urllib.parse
import re
import lyricsgenius
from alive_progress import alive_bar


class HiddenPrints:
    def __enter__(self):
        """
        Suppress printing output
        """
        self._original_stdout = sys.stdout
        sys.stdout = open(os.devnull, "w")

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Exit suppress printing output
        """
        sys.stdout.close()
        sys.stdout = self._original_stdout


def get_lyrics_from_Genius(genius, title, artist):
    """
    Find lyrics of song using Genius API

    Parameters
    ----------
    title : string
        song title
    artist : string
        artist of song

    Returns
    ----------
    lyrics : dict
        return dictionary with keys: title, artist and lyrics
    """
    with HiddenPrints():
        song = genius.search_song(title, artist)
        if song:
            lyrics = song.lyrics
            return lyrics


def extract_lyrics(token, song_title, artist):
    """
    Extracting lyrics for a song

    Parameters
    ----------
    song_title : string
        Title of the song
    artist : string
        Artist of the song
    token : string
        A token from Genius for asccessing lyrics

    Returns
    ----------
    songs : dataframe
        Return lyrics of song with three columns: song_title, artist and lyrics
    """
    try:
        genius = lyricsgenius.Genius(token, retries=5)

        if song_title == "" or artist == "":
            raise ValueError("Empty input")

        if not (type(song_title) == str and type(artist) == str):
            raise ValueError(
                "Invalid column type, song title and artist have to be strings"
            )

        print("Checking URL connection...")

        lyrics = get_lyrics_from_Genius(
            genius,
            song_title,
            artist,
        )

        if lyrics:
            songs = {}
            songs["song_title"] = song_title
            songs["artist"] = artist
            songs["lyrics"] = lyrics

        return songs

    except Exception as req:
        print(req)


"""
## --For later milestones
# test
# /data/credentials.json
# {
#   "token": "YOUR-TOKEN"
# }

with open("data/credentials.json") as f:
    login = json.load(f)
token = login["token"]

# Case 1 - happy case
arr_happy = ["22", "Taylor Swift"]

# Case 2 - empty dataframe
arr_edge1 = ["", "Taylor Swift"]

# Case 3 - Wrong types
arr_wrong_type = [22, "Taylor Swift"]


print("1 - Happy:")
print(extract_lyrics(token, arr_happy[0], arr_happy[1]), "\n")
print("2 - Empty:")
print(extract_lyrics(token, arr_edge1[0], arr_edge1[1]), "\n")
print("7 - Wrong column types:")
print(extract_lyrics(token, arr_wrong_type[0], arr_wrong_type[1]), "\n")
"""
