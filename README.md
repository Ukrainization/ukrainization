# Ukrainization

Ukrainization is a Python library for working with ukrainian text.

## Installation

You will be able to install this package by pip on future. Now, you can install by github link.

```bash
pip install https://github.com/Ukrainization/ukrainization.git
```

## Usage

```python
from normalization.lemmatization import UkLemmatizer

lemm = UkLemmatizer()
token = 'чорніє'
result = lemm.token_lemmatization(token=token)
print(result)  # return 'чорніти'
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

GNU GENERAL PUBLIC LICENSE

## References

1. Korobov M.: *Morphological Analyzer and Generator for Russian and Ukrainian Languages* // Analysis of Images, Social Networks and Texts, pp 320-332 (2015). [Link](https://pypi.org/project/pymorphy2/)
2. Eunjoo Byeon: *How to Efficiently Remove Punctuations from a String* (2020). [Link](https://towardsdatascience.com/how-to-efficiently-remove-punctuations-from-a-string-899ad4a059fb)
3. Vladislav Klim: *Ukrainian Stemmer* (Oct 2019). [Link](https://github.com/Desklop/Uk_Stemmer)

