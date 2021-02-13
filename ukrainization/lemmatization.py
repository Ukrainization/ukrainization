import pymorphy2

__version__ = 1.0


class UkLemmatizer:

    def __init__(self):
        self.morph = pymorphy2.MorphAnalyzer(lang='uk')
    
    def token_lemmatization(self, token):
        """
        input: token (one word)
        output: lemmitized token (simple word form)
        """
        return self.morph.parse(token)[0].normal_form
