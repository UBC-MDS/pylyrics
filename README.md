# Python package for extract and analyse lyrics  

-   Author: Abhiket Gaurav, Artan Zandian, Macy Chan, Manju Abhinandana Kumar


### Overview
(TBC)  
This package helps you extract and analyse lyrics like a piece of cake!   



### Functions

| Function Name | Input | Output | Description |
|-----------|------------|---------------|------------------|
| download_data | `url`, `cols` | cols | Download csv file from `url` and extract `cols` into a Pandas DataFrame with `cols` name|
| extract_lyrics | `song_title`, `artist` | String | Extract song lyrics of `song_title` by `artist`  |
| clear_text | `paragraph`, `vocabs` | String |  Clean the `paragraph` with provided `vocabs` |
| plot_cloud | `song_titles`, `artists` | Word Cloud | Show word cloud of lyrics of input `song_titles` and `artists` |


### Our Package in the Python Ecosystem
There exist similar packages Python. However, this package is more holistic, in the sense that it downloads the lyrics through APIs, cleans the text, and then makes the word cloud. There are packages which does one of these steps. This package takes care of all the steps. Of the many other similar packages, the following are the two examples that come close: https://github.com/lorenza12/Cloud-Lyrics and https://deezer.io/a-new-way-to-look-at-an-artist-from-lyrics-to-wordclouds-christmas-special-56a854cb4e77#.op1gx82h4



### Installation

```bash
$ pip install pylyrics
```

### Features
(TBC)  
1.Download the data
Input : url (csv) & col you wanna extract
Output : DataFrame with input cols

2. Extract lyrics from API
Input : song_title[0], artist[0]
Output : lyrics

3. Clear text
Input : paragraph, list[voacb]
Output : cleaned paragraph

4. Plot WordCloud
Input: song_title[], artist[]
Const: Min 1; Max 5
make use of (2) & (3)
Output : A WordCloud

[a bulleted list of the functions (and datasets if applicable) that will be included in the package (this should be a 1-2 sentence description for each function/dataset)]


### Dependencies
(TBC)  
- python = ^3.9
- pandas = ^1.2.3
- regex = ^2020.11.13
- json
- urllib.parse
- lyricsgenius
- tqdm.notebook 


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
