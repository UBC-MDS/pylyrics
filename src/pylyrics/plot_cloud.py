# Authors: Abhiket Gaurav, Artan Zandian, Macy Chan, Manju Abhinandana Kumar
# January 2022

from pylyrics import extract_lyrics
from pylyrics import clean_text

from wordcloud import WordCloud
import matplotlib.pyplot as plt


def plot_cloud(
    song,
    file_path,
    max_font_size=30,
    max_words=120,
    background_color="black",
    show=False,
):
    """
    Creates a wordcloud of most occuring words in a string or list of strings

    Parameters
    ----------
    song: dictionary
        with artist as dictionary key and song_title as value. Both key and value are strings.
    file_path: str
        The location to save the file
    max_font_size: int, optional
        maximum font size
    max_words: int, optional
        maximum number of words to be included in wordcloud
    background_color: str, optional
        background color
    show: bool, default=False
        whether to display the plot to screen

    Returns
    -------
    image
        A wordcloud image supported by matplotlib

    Example
    -------
    >>> from pylyrics.pylyrics import plot_cloud
    >>> plot_cloud(song, file_path, max_font_size=30, max_words=100, background_color='black', show=True)

    """

    ## Exception Handeling to be added

    text = ""
    # Create a string of all song lyrics
    for artist, song_title in song.items():
        raw_lyrics = extract_lyrics(artist, song_title)
        clean_lyrics = clean_text(text=raw_lyrics)
        text += " " + clean_lyrics  # Adding space for the end of lyrics

    # plot the wordcloud
    wordcloud = WordCloud(
        max_font_size=max_font_size,
        max_words=max_words,
        background_color=background_color,
    ).generate(text)
    plt.imshow(wordcloud, interpolation="antialiased")
    plt.axis("off")

    if show:
        plt.show()

    plt.savefig(file_path)
