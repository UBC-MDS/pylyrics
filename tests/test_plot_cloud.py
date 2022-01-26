# Authors: Abhiket Gaurav, Artan Zandian, Macy Chan, Manju Abhinandana Kumar
# Date: 2022-01-20

from pylyrics import plot_cloud as pc
import pytest
import os

# Skip testing this module if on Github Actions
ON_GITHUB_ACTIONS = '/home/runner' in os.path.expanduser('~') or '/Users/runner' in os.path.expanduser('~')  or 'C:\\Users\\runner' in os.path.expanduser('~')


@pytest.fixture
def correct_values():
    song = {"Taylor Swift": "22", "Queen": "Bohemian Rhapsody"}
    file_path = "tests/data/22_BR"
    return song, file_path

# Testing input values are of correct type
def test_input_types(correct_values):
    with pytest.raises(TypeError):
        _, file_path = correct_values
        wrong_song_type = ["22", "Taylor Swift"]
        pc.plot_cloud(wrong_song_type, file_path)  # should be dict

    with pytest.raises(TypeError):
        song, _ = correct_values
        wrong_file_path = 2
        pc.plot_cloud(song, wrong_file_path)  # should be str

    with pytest.raises(TypeError):
        song, file_path = correct_values
        pc.plot_cloud(song, file_path, background_color=23)  # should be str

    with pytest.raises(TypeError):
        song, file_path = correct_values
        pc.plot_cloud(song, file_path, max_font_size="ten")  # should be int

    with pytest.raises(TypeError):
        song, file_path = correct_values
        pc.plot_cloud(song, file_path, max_words="ten")  # should be int


# Testing the case when no lyrics is found
def test_no_lyrics(correct_values):
    with pytest.raises(ValueError):
        _, file_path = correct_values
        song = {"22": "Queen"}
        pc.plot_cloud(song, file_path)


# Testing if an image is saved
@pytest.mark.skipif(ON_GITHUB_ACTIONS, reason='Requires access to the Genius website.')
def test_image(correct_values):
   song, file_path = correct_values
   pc.plot_cloud(song, file_path)
   assert os.path.exists(file_path + ".png") == True, "No image has been saved"
