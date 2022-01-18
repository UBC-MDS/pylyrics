# Authors: Abhiket Gaurav, Artan Zandian, Macy Chan, Manju Abhinandana Kumar
# Date: 2022-01-14

import os, sys
import lyricsgenius


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

    Example
    -------
    >>> get_lyrics_from_Genius(genius, "22", "Taylor Swift")
    >>> "[Verse 1]\nIt feels like a perfect night\nTo dress u..."
    """

    with HiddenPrints():
        song = genius.search_song(title, artist)
        if song:
            lyrics = song.lyrics
            return lyrics


def get_lyrics(token, song_title, artist):
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

    Example
    -------
    >>> extract_lyrics("I-AM-TOKEN", "22", "Taylor Swift"):
    >>> "[Verse 1]\nIt feels like a perfect night\nTo dress u..."

    """
    try:
        genius = lyricsgenius.Genius(token, retries=5)

        if song_title == "" or artist == "":
            raise ValueError("Empty input")

        if not (type(song_title) == str and type(artist) == str):
            raise TypeError(
                "Invalid column type, song title and artist have to be strings"
            )

        lyrics = get_lyrics_from_Genius(
            genius,
            song_title,
            artist,
        )

        if lyrics:
            return lyrics

    except ValueError as err:
        #print(err)
        raise
