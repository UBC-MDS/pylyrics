# Pylyrics  
A Python package to extract and analyze lyrics

-   Authors: Abhiket Gaurav, Artan Zandian, Macy Chan, Manju Abhinandana Kumar


### Overview
This package allows users to extract and analyze lyrics effortlessly. With pylrics users can download songs attribute datasets from Kaggle, extract lyrics and generate a word cloud. 



### Functions

| Function Name | Input | Output | Description |
|-----------|------------|---------------|------------------|
| download_data | `kaggle dataset`, `filepath`, `columns` | cols | Download dataset from `kaggle dataset` and extract `columns` from csv file into a Pandas DataFrame |
| extract_lyrics | `song_title`, `artist` | String | Extract song lyrics of `song_title` by `artist`  |
| clear_text | `paragraph`, `vocabs` | String |  Clean up the `paragraph` with provided `vocabs` |
| plot_cloud | `song_titles`, `artists` | figure | Show word cloud of lyrics of input `song_titles` and `artists` |


### Our Package in the Python Ecosystem
There exist similar packages Python. However, this package is more holistic, in the sense that it downloads the lyrics through APIs, cleans the text, and then makes the word cloud. There are packages which does one of these steps. This package takes care of all the steps. Of the many other similar packages, the following are the two examples that come close: https://github.com/lorenza12/Cloud-Lyrics and https://deezer.io/a-new-way-to-look-at-an-artist-from-lyrics-to-wordclouds-christmas-special-56a854cb4e77#.op1gx82h4



### Installation

```bash
$ pip install pylyrics
```

### Features
The pylyrics packages contains the following four functions:

1.`download_data()` The download data function downloads dataset from Kaggle, extracts the given columns from csv file and creates a dataframe.

2. `extract_lyrics()` The extract lyrics function, extracts the lyrics from API for a song title and artist and saves it as a dataframe with columns song title, artist and lyrics.

3. `clean_text()` The lyrics extracted from extract_lyrics() are not clean. It removes attribute tags like chorus etc , punctuations and English stop words to get a cleaned paragraph. 

4. `plot_cloud` The plot cloud function creates a word cloud of most occuring words in a song/songs by an artist.


### Dependencies
- python = ^3.9
- pandas = ^1.2.3
- regex
- kaggle
- json
- urllib.parse
- lyricsgenius
- alive_progress
- wordcloud
- matplotlib

### Usage
(TBC)


### Documentation

The official documentation is hosted on Read the Docs: [Link TBC]

## Contributors
The names of core development team is listed below.

| Name |
|------|
| Abhiket Gaurav |  
| Artan Zandian | 
| Macy Chan | 
| Manju Abhinandana Kumar |  

We welcome and recognize all contributions. Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

### License

`pylyrics` was created by Group 2. It is licensed under the terms of the MIT license.

### Credits

`pylyrics` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
