# Ukrainization

Ukrainization is a Python library for working with ukrainian text.

## Installation

You will be able to install this package by pip on future. Now, you can install by github link.

```bash
pip install https://github.com/Ukrainization/ukrainization.git
```

## Usage

```python
from linguist.lemmatization import UkLemmatizer

lemm = UkLemmatizer()
token = 'чорніє'
result = lemm.token_lemmatization(token=token)
print(result) # return 'чорніти'
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

GNU GENERAL PUBLIC LICENSE