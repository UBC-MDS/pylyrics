from pylyrics import plot_cloud as pc
import pytest

# Case 1 - wrong input types
def test_input_types():
    try:
        wrong_song_type = ["22", "Taylor Swift"]
        file_path = "image.png"
        assert pc.plot_cloud(wrong_song_type, file_path) == ValueError


 

# Case 2 - show True or False
def test_show_true():
    # How can I get the interim output of a function (plot to screen)?
    assert isinstance(fig, ...), ""


# Case 3 - no_lyrics found
def test_no_lyrics():



# Case 4 - image printed
def test_no_image():
    with pc.plot_cloud(wrong_song_type, file_path) as fig:
        assert isinstance(fig, ...), "Invalid image type"