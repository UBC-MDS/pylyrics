# Authors: Abhiket Gaurav, Artan Zandian, Macy Chan, Manju Abhinandana Kumar
# January 2022

from pylyrics import clean_text as ct
import pytest

# Case 1 -happy case
def test_happy_case():
    lyrics = "It feels like a perfect night To dress up like hipsters And make fun of our exes"
    target = "it feels like a perfect night to dress up like hipsters and make fun of our exes"
    assert ct.clean_text(lyrics) == target, "Incorrect return value"


# Case 2 - empty dataframe
def test_empty_case():
    lyrics = " "
    with pytest.raises(ValueError):
        ct.clean_text(lyrics)


# Case 3 - Wrong input type for bool_contra_dict
def test_wrong_type_case():
    lyrics = "an"
    with pytest.raises(TypeError):
        ct.clean_text(lyrics, "aaaa")


# Case 4 - Wrong input type for lyrics
def test_wrong_input_case():
    lyrics = 22
    with pytest.raises(TypeError):
        ct.clean_text(lyrics)
