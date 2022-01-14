# author: Macy Chan
# date: 2022-01-14

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
    lyrics : string
        lyrics of song
    """
    with HiddenPrints():
        song = genius.search_song(title, artist)
        if song:
            lyrics = song.lyrics
            return lyrics


def extract_lyrics(token, songs):
    """
    Extracting lyrics for a maximum of 5 songs

    Parameters
    ----------
    songs : dataframe
        A dataframe consists two columns: song_title and artist
    token : string
        A token from Genius for asccessing lyrics

    Returns
    ----------
    songs : dataframe
        Return lyrics of song with three columns: song_title, artist and lyrics
    """
    try:
        genius = lyricsgenius.Genius(token, retries=5)

        if songs.empty:
            raise ValueError("Empty DataFrame")

        if len(songs) > 5:
            raise ValueError("Only accept song lists short than 5 songs or below")

        if not ("song_title" in songs and "artist" in songs):
            raise ValueError(
                "Invalid column names, please provide song_title and artist"
            )

        if not (
            songs["song_title"].dtypes == "object"
            and songs["artist"].dtypes == "object"
        ):
            raise ValueError(
                "Invalid column names, please provide song_title and artist"
            )

        songs["lyrics"] = ""

        print("Checking URL connection...")
        with alive_bar(len(songs), bar="bubbles", spinner="notes2") as bar:
            for i in range(len(songs)):
                lyrics = get_lyrics_from_Genius(
                    genius,
                    songs.iloc[i]["song_title"],
                    songs.iloc[i]["artist"],
                )

                if lyrics:
                    songs["lyrics"][i] = lyrics
                bar()

        return songs

    except Exception as req:
        print(req)


""" --For later milestones
# test
# /data/credentials.json
# {
#   "token": "YOUR-TOKEN"
# }

with open("data/credentials.json") as f:
    login = json.load(f)
token = login["token"]

# Case 1 - happy case
df_happy = pd.DataFrame(
    {
        "song_title": ["22", "POV"],
        "artist": ["Taylor Swift", "Ariana Grande"],
    }
)

# Case 2 - empty dataframe
df_edge1 = pd.DataFrame(
    {
        "song_title": [],
        "artist": [],
    }
)

# Case 3 - six row
df_edge2 = pd.DataFrame(
    {
        "song_title": [
            "22",
            "POV",
            "Easy On Me",
            "abcdefu",
            "Ghost",
            "All Too Well",
            "Bad Habit",
        ],
        "artist": [
            "Taylor Swift",
            "Ariana Grande",
            "Adele",
            "GAYLE",
            "Justin Bieber",
            "Taylor Swift",
            "Ed Sheeran",
        ],
    }
)

# Case 4 - Extra columns
df_extra_cols = pd.DataFrame(
    {
        "song_title": ["22", "POV"],
        "artist": ["Taylor Swift", "Ariana Grande"],
        "popularity": [999, 100],
    }
)

# Case 5 - Missing columns
df_missing_cols = pd.DataFrame(
    {
        "artist": ["Taylor Swift", "Ariana Grande"],
    }
)

# Case 6 - Wrong columns name
df_wrong_name = pd.DataFrame(
    {
        "song_title_1": ["22", "POV"],
        "artist": ["Taylor Swift", "Ariana Grande"],
    }
)

# Case 7 - Wrong column types
df_wrong_type = pd.DataFrame(
    {
        "song_title": [22, 3435],
        "artist": ["Taylor Swift", "Ariana Grande"],
    }
)

# Case 8 - Invalid Song name
df_invalid = pd.DataFrame(
    {
        "song_title": ["AAAA", "A"],
        "artist": ["AAA", "AAA"],
    }
)

print("1 - Happy:")
print(extract_lyrics(token, df_happy), "\n")
print("2 - Empty:")
print(extract_lyrics(token, df_edge1), "\n")
print("3 - Six inputs:")
print(extract_lyrics(token, df_edge2), "\n")
print("4 - Extra columns:")
print(extract_lyrics(token, df_extra_cols), "\n")
print("5 - Missing columns:")
print(extract_lyrics(token, df_missing_cols), "\n")
print("6 - Wrong columns name:")
print(extract_lyrics(token, df_wrong_name), "\n")
print("7 - Wrong column types:")
print(extract_lyrics(token, df_wrong_type), "\n")
print("8 - Invalid:")
print(extract_lyrics(token, df_invalid), "\n")
"""
