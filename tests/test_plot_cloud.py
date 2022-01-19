from pylyrics import plot_cloud as pc
import pytest
import os



@pytest.fixture
def correct_values():
    song = {"22": "Taylor Swift",
            "Bohemian Rhapsody": "Queen"    
            }
    file_path = os.getcwd() + "/tests/data/22.jpg"

    return song, file_path


def test_input_types(correct_values):
    """Test wrong input types"""

    with pytest.raises(TypeError):
        _ , file_path = correct_values
        wrong_song_type = ["22", "Taylor Swift"]
        pc.plot_words(wrong_song_type, file_path)  # should be dict

    with pytest.raises(TypeError):
        song , _ = correct_values
        wrong_file_path = 2
        pc.plot_words(song, wrong_file_path)  # should be str

    with pytest.raises(TypeError):
        song , file_path = correct_values
        pc.plot_words(song , file_path, background_color=23)  # should be string

    with pytest.raises(TypeError):
        song , file_path = correct_values
        pc.plot_words(song , file_path, max_font_size=True)  # should be int

    with pytest.raises(TypeError):
        song , file_path = correct_values
        pc.plot_words(song , file_path, max_words=True)  # should be int

    with pytest.raises(TypeError):
        song , file_path = correct_values
        pc.plot_words(song , file_path, show="yes")  # should be boolean
 

# Case 2 - show True or False
def test_show_true():
    # How can I get the interim output of a function (plot to screen)?
    assert isinstance(fig, ...), ""


# Case 3 - no_lyrics found
def test_no_lyrics():



# Case 4 - image printed
def test_no_image():
    fig = pc.plot_cloud(wrong_song_type, file_path)
    assert isinstance(fig, ...), "Invalid image type"