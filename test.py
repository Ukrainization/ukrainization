print("hello Ukrainization!!!")


from linguist.lemmatization import UkLemmatizer
from preparator.preparation import remove_punctuation, to_lowe_case


lemm = UkLemmatizer()

token = 'чорніє'
result = lemm.token_lemmatization(token=token)
print(result)

sentence = 'Дорогу сестру збираю у дорогу а брати вирішили не брати машину'
result = lemm.tokens_lemmatization(tokens=sentence.split(" "))
print(result)

sentence = "Слов'янське слово «Україна» вперше згадується у Київському літописному зводі за Іпатіївським списком під 1187 роком."
result = remove_punctuation(sentence)
print(result)
result = to_lowe_case(sentence)
print(result)


# Useful links
# https://datascience.stackexchange.com/questions/16786/is-there-a-process-flow-to-follow-for-text-analytics
# https://www.accenture.com/us-en/blogs/search-and-content-analytics-blog/natural-language-processing-techniques
# TODO: rename linguist folder to => Normalization
# TODO: add Stemming
# TODO: Add Remove stop-words