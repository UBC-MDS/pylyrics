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
    try:
        arr_edge1 = ["", "Taylor Swift"]
        with pytest.raises(ValueError):
            pl.extract_lyrics(arr_edge1[0], arr_edge1[1])
        assert (
            pl.extract_lyrics(arr_edge1[0], arr_edge1[1]) == None
        ), "Edge case exception handling failed, should return None"
    except:
        assert True


# Case 3 - Wrong types
def test_wrong_type_case():
    try:
        arr_wrong_type = [22, "Taylor Swift"]
        with pytest.raises(TypeError):
            pl.extract_lyrics(arr_wrong_type[0], arr_wrong_type[1])
        assert (
            pl.extract_lyrics(arr_wrong_type[0], arr_wrong_type[1]) == None
        ), "Type check exception handling failed, should return None"
    except:
        assert True


# Case 4 - None from Genius
def test_null_genius_case():
    try:
        arr_null_genius = ["222", "1111"]
        with pytest.raises(ValueError):
            print(pl.extract_lyrics(arr_null_genius[0], arr_null_genius[1]))
        assert (
            pl.extract_lyrics(arr_null_genius[0], arr_null_genius[1]) == None
        ), "Song not found"
    except:
        assert True


test_happy_case()
test_empty_case()
test_wrong_type_case()
test_null_genius_case()
