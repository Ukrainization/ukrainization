import pymorphy2

class UkLemmatizer():

    def __init__(self):
        self.morph = pymorphy2.MorphAnalyzer(lang='uk')
    
    def token_lemmatization(self, token):
        """
        input: token (one word)
        output: lemmitized token (simple word form)
        """
        return self.morph.parse(token)[0].normal_form

    
    def tokens_lemmatization(self, tokens):
        """
        input: tokens list of sentence/text without punctuation
        output: lemmitized tokens list 
        """
        lemmitized_tokens = []
        for word in tokens:
            result = self.morph.parse(word)[0].normal_form
            lemmitized_tokens.append(result)
        return lemmitized_tokens

