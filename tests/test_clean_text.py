# Authors: Abhiket Gaurav, Artan Zandian, Macy Chan, Manju Abhinandana Kumar
# January 2022

from pylyrics import clean_text as ct
import pytest
import re

# Case 1
def test_case1():
    lyrics = "It feels like a perfect night To dress up like hipsters And make fun of our exes"
    target = "it feels like a perfect night to dress up like hipsters and make fun of our exes"
    assert ct.clean_text(lyrics) == target, "Something went wrong"


# Case 2 - empty dataframe
def test_case2():
    lyrics = " "
    with pytest.raises(ValueError):
        ct.clean_text(lyrics)


# Case 3 - wrong type
def test_case3():
    try:
        lyrics = "!!I Love you"
        with pytest.raises(TypeError):
            regex = re.compile("[@_!#$%^&*()<>?/|}{~:]")
            subtext = ct.clean_text(lyrics)[0:1]
        assert regex.search(subtext) != None, "Text cannot start with special character"
    except:
        assert True


# Case 4 - small text
def test_case4():
    try:
        lyrics = "!!I Love you"
        assert len(ct.clean_text(lyrics)) <= 5, "Too small to give meaniful output"
    except:
        assert True
