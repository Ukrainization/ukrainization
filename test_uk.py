# py.test -p no:warnings

from normalization.lemmatization import UkLemmatizer
from preparator.preparation import remove_punctuation, to_lowe_case
from normalization.stemming import UkStemmer


def test_token_lemmatization_noun():
    token = 'пташкою'
    lemm = UkLemmatizer()
    assert lemm.token_lemmatization(token) == 'пташка'


def test_token_lemmatization_adj():
    token = 'малого'
    lemm = UkLemmatizer()
    assert lemm.token_lemmatization(token) == 'малий'


def test_token_lemmatization_obj():
    token = 'Саша'
    lemm = UkLemmatizer()
    assert lemm.token_lemmatization(token) == 'саша'


def test_tokens_lemmatization():
    sentence = 'Кіт невеликий ссавець ряду хижих родини котячих'
    tokens = sentence.split(" ")
    result = ['кіт', 'невеликий', 'ссавець', 'ряд', 'хижий', 'родина', 'котячий']
    lemm = UkLemmatizer()
    assert lemm.tokens_lemmatization(tokens) == result


def test_remove_punctuation():
    sentence = "...Чи знайомі ви з романом Панаса Мирного «Хіба ревуть воли, як ясла повні?»"
    assert remove_punctuation(sentence) == "Чи знайомі ви з романом Панаса Мирного Хіба ревуть воли як ясла повні"


def test_to_lowe_case():
    text = 'ПриВіт як СПРАВИ'
    assert to_lowe_case(text) == 'привіт як справи'


def test_stem_word():
    word = 'коти'
    stem = UkStemmer()
    assert stem.stemWord(word) == 'кот'
