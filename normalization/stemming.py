import re

__version__ = 1.0


class UkStemmer:
    def __init__(self):
        """
        Useful links:
         - vowel: uk.wikipedia.org/wiki/Голосний_звук
         - perfectiveground: uk.wikipedia.org/wiki/Рефлексивне_дієслово
         - adjective: uk.wikipedia.org/wiki/Прикметник + wapedia.mobi/uk/Прикметник
         - participle: uk.wikipedia.org/wiki/Дієприкметник
         - verb: http://uk.wikipedia.org/wiki/Дієслово
         - noun: uk.wikipedia.org/wiki/Іменник
         - Code: https://github.com/Desklop/Uk_Stemmer/blob/master/uk_stemmer/uk_stemmer.py
        """
        self.vowel = r'аеиоуюяіїє'
        self.perfectiveground = r'(ив|ивши|ившись|ыв|ывши|ывшись((?<=[ая])(в|вши|вшись)))$'
        self.reflexive = r'(с[яьи])$'
        self.adjective = r'(ими|ій|ий|а|е|ова|ове|ів|є|їй|єє|еє|я|ім|ем|им|ім|их|іх|ою|йми|іми|у|ю|ого|ому|ої)$'
        self.participle = r'(ий|ого|ому|им|ім|а|ій|у|ою|ій|і|их|йми|их)$'
        self.verb = r'(сь|ся|ив|ать|ять|у|ю|ав|али|учи|ячи|вши|ши|е|ме|ати|яти|є)$'
        self.noun = r'(а|ев|ов|е|ями|ами|еи|и|ей|ой|ий|й|иям|ям|ием|ем|ам|ом|о|у|ах|иях|ях|ы|ь|ию|ью|ю|ия|ья|я|і|ові|ї|ею|єю|ою|є|еві|ем|єм|ів|їв|ю)$'
        self.rvre = r'[аеиоуюяіїє]'
        self.derivational = r'[^аеиоуюяіїє][аеиоуюяіїє]+[^аеиоуюяіїє]+[аеиоуюяіїє].*(?<=о)сть?$'
        self.RV = ''

    def __ukstemmer_search_preprocess(self, word):
        word = word.lower()
        word = word.replace("'", "")
        word = word.replace("ё", "е")
        word = word.replace("ъ", "ї")
        return word

    def __s(self, st, reg, to):
        orig = st
        self.RV = re.sub(reg, to, st)
        return (orig != self.RV)

    def stem_word(self, word):
        ''' Find the basis (stem) of a word.
        1. word - source word (UTF-8 encoded string)
        2. returns the stemmed form of the word (UTF-8 encoded string) '''

        word = self.__ukstemmer_search_preprocess(word)
        if not re.search('[аеиоуюяіїє]', word):
            stemma = word
        else:
            p = re.search(self.rvre, word)
            start = word[0:p.span()[1]]
            self.RV = word[p.span()[1]:]

            # Step 1
            if not self.__s(self.RV, self.perfectiveground, ''):

                self.__s(self.RV, self.reflexive, '')
                if self.__s(self.RV, self.adjective, ''):
                    self.__s(self.RV, self.participle, '')
                else:
                    if not self.__s(self.RV, self.verb, ''):
                        self.__s(self.RV, self.noun, '')
            # Step 2
            self.__s(self.RV, 'и$', '')

            # Step 3
            if re.search(self.derivational, self.RV):
                self.__s(self.RV, 'ость$', '')

            # Step 4
            if self.__s(self.RV, 'ь$', ''):
                self.__s(self.RV, 'ейше?$', '')
                self.__s(self.RV, 'нн$', u'н')

            stemma = start + self.RV
        return stemma

    def stemWord(self, word):
        ''' Find the basis (stem) of a word.
        1. word - source word (UTF-8 encoded string)
        2. returns the stemmed form of the word (UTF-8 encoded string)

        This method is used to simulate the PyStemmer interface (https://github.com/snowballstem/pystemmer). '''

        return self.stem_word(word)
