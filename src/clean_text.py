# Authors: Abhiket Gaurav, Artan Zandian, Macy Chan, Manju Abhinandana Kumar
# January 2022

import re
from pylyrics import extract_lyrics


def clean_text(text):
    """Cleans the text by removing special characters, html_tags, #tags, contaction words.

    Parameters
    ----------
    text : str
        Text to clean.

    Returns
    -------
    str
        Cleaned text.

    Examples
    --------
    >>> clean_text("Early optimization is the root of all evil!")
    'early optimization is the root of all evil'
    """
    ## Exception Handeling to be added

    contra_dict={"'s":" is","n't":" not","'m":" am","'ll":" will",
           "'d":" would","'ve":" have","'re":" are"}
    #replace the contractions
    for key,value in contra_dict.items():
        if key in text:
            text = text.replace(key,value)
    # lower case and remove special characters
    text = re.sub(r'[^a-zA-Z\s]', '', text, re.I|re.A)
    text = re.sub(r'https?:\/\/.\S+', "", text)
    text = re.sub(r'#', '', text)
    text = text.lower()
    
    return text