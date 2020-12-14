import string

PUNCTUATION = string.punctuation + string.digits + '«»'

def remove_punctuation(text_corpus):
    """
    Return text without punctuation
    Link: https://towardsdatascience.com/how-to-efficiently-remove-punctuations-from-a-string-899ad4a059fb
    """
    table_ = str.maketrans('', '', PUNCTUATION)
    return text_corpus.translate(table_)


def to_lowe_case(text_corpus):
    """
    Conver upper case to lower case
    """
    return text_corpus.lower()