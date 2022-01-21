from pylyrics import download_data as dd
import pandas as pd
import pytest
import os


def test_input_types():
    """Test for input types"""

    with pytest.raises(TypeError):
        file_path = os.getcwd() + "/tests/data/"
        columns = ["song_title", "artist"]
        dd.download_data(1, "file_path", columns)  # dataset: should be string

    with pytest.raises(TypeError):
        dataset = "geomack/spotifyclassification"
        columns = ["song_title", "artist"]
        dd.download_data(dataset, 1, columns)  # filepath: should be string

    with pytest.raises(TypeError):
        dataset = "geomack/spotifyclassification"
        file_path = os.getcwd() + "/tests/data/"
        columns = "song_title"
        dd.download_data(dataset, "file_path", columns)  # columns: should be a list

    with pytest.raises(TypeError):
        dataset = "geomack/spotifyclassification"
        file_path = os.getcwd() + "/tests/data/"
        columns = ["song_title"]
        dd.download_data(
            dataset, "file_path", columns
        )  # columns: should be a list of length 2


def test_dataframe():
    dataset = "geomack/spotifyclassification"
    filepath = "tests/data/spotify_attributes"
    columns = ["song_title", "artist"]
    # assert isinstance(download_data(dataset, filepath, columns),pd.DataFrame) == True, "Should return a dataframe"
    assert (
        len(dd.download_data(dataset, filepath, columns).columns) == 2
    ), "Should return a dataframe with 2 columns"


def test_output():
    with pytest.raises(ValueError):
        dataset = "geomack/spotifyclassification"
        filepath = "tests/data/spotify_attributes"
        columns = ["song", "artist"]
        dd.download_data(dataset, filepath, columns)  # Columns names are incorrect
