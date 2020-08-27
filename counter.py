#usr/bin/env python3 
#counter.py

def word_counter(string: str) -> int:
    """ 
        this function get number of all words in a text
    """

    words = string.split();
    return len(words)

def character_counter(string: str) -> int:
    """ 
        this function get number all characters in a text
    """
    
    string = string.strip()
    return len(string)