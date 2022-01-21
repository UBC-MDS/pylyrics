from pylyrics import extract_lyrics as pl
import json, os
import pytest


# Case 1 - happy case
def test_happy_case():
    current_path = os.getcwd()
    arr_happy = ["22", "Taylor Swift"]
    target = open(current_path + "/tests/data/lyrics_22.txt", "r").read()
    assert (
        pl.extract_lyrics(arr_happy[0], arr_happy[1]) == target
    ), "Lyrics output incorrect"


# Case 2 - empty dataframe
def test_empty_case():
    arr_edge1 = ["", "Taylor Swift"]
    with pytest.raises(ValueError):
        pl.extract_lyrics(arr_edge1[0], arr_edge1[1])


# Case 3 - Wrong types
def test_wrong_type_case():

    arr_wrong_type = [22, "Taylor Swift"]
    with pytest.raises(TypeError):
        pl.extract_lyrics(arr_wrong_type[0], arr_wrong_type[1])


# Case 4 - None from Genius
def test_null_genius_case():
    arr_null_genius = ["222", "1111"]
    with pytest.raises(ValueError):
        print(pl.extract_lyrics(arr_null_genius[0], arr_null_genius[1]))
