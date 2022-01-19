from pylyrics import plot_cloud as pc
import matplotlib as plt
import pytest
import os


@pytest.fixture
def correct_values():
    song = {"22": "Taylor Swift", "Bohemian Rhapsody": "Queen"}
    file_path = os.getcwd() + "/tests/data/22_BR"

    return song, file_path


def test_input_types(correct_values):
    """Test wrong input types"""

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

    with pytest.raises(TypeError):
        song, file_path = correct_values
        pc.plot_cloud(song, file_path, show="yes")  # should be boolean


def test_show_true():
    """Testing the branching of show argument to see if image is generated"""
    song, file_path = correct_values
    fig = pc.plot_cloud(song, file_path, show=True)
    assert isinstance(fig, plt.figure), "No plot has been printed to the screen"
    # Need to check if plt.figure.Figure works


def test_no_lyrics(correct_values):
    """Testing the case when no lyrics is found"""
    with pytest.raises(ValueError):
        _, file_path = correct_values
        song = {"22": "Queen"}
        pc.plot_cloud(song, file_path)


def test_image(correct_values):
    """Testing if an image is saved"""
    song, file_path = correct_values
    pc.plot_cloud(song, file_path)
    saved_img = open(file_path + ".png").read()
    assert saved_img == True, "No image has been saved"
