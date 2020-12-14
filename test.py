print("hello Ukrainization!!!")


from linguist.lemmatization import UkLemmatizer

lemm = UkLemmatizer()

token = 'чорніє'


result = lemm.token_lemmatization(token=token)
print(result)

sentence = 'Дорогу сестру збираю у дорогу а брати вирішили не брати машину'

result = lemm.tokens_lemmatization(tokens=sentence.split(" "))

print(result)

