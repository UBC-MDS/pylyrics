from pylyrics import download_data
import pandas as pd
import pytest
import os


def test_dataframe():
    assert isinstance(download_data("geomack/spotifyclassification",
                              "data/spotify_attributes", 
                              ["song_title", "artist"]),pd.DataFrame) == True, "Should return a dataframe"
    
    assert len(download_data("geomack/spotifyclassification",
                              "data/spotify_attributes", 
                              ["artist", "song_title"]).columns) == 2, "Should return a dataframe with 2 columns"
    
    assert set(("artist", "song_title")).issubset(
        download_data("geomack/spotifyclassification",
                              "data/spotify_attributes", 
                              ["artist", "song_title"]).columns) == True, "Columns names are incorrect"