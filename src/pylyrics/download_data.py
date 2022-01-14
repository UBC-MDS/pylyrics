# Authors: Abhiket Gaurav, Artan Zandian, Macy Chan, Manju Abhinandana Kumar
# January 2022

import os
import pandas as pd
import kaggle

def download_data(dataset, file_path, columns):
    """
    Downloads dataset from kaggle to filepath and creates a dataframe with input columns

    Parameters
    ----------
    dataset: str
        kaggle dataset name to download
    file_path: str
        location to save the file
    columns: list
        list of columns to create a dataframe

    Returns
    -------
    dataframe:
        A dataframe with the given column names

    Example
    -------
    from pylyrics import download_data
    download_data("geomack/spotifyclassification", "data/spotify_attributes", ("song_title", "artist"))
    spotify_df = download_data("geomack/spotifyclassification", "data/spotify_attributes", ("song_title", "artist"))
    """
    try:
        kaggle.api.authenticate()
        kaggle.api.dataset_download_files(
            dataset,
            path=file_path,
            unzip=True,
        )
    except:
        os.makedirs(os.path.dirname(file_path))
        kaggle.api.authenticate()
        kaggle.api.dataset_download_files(
            dataset,
            path=file_path,
            unzip=True,
        )
    
    df = pd.read_csv((file_path + '/' + str(os.listdir(file_path).pop())), usecols=columns)
    return df