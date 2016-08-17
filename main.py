import re
from itertools import chain, zip_longest


def reverse(st):
    words = re.findall(r'\w+', st)
    response = ''

    for i, word in enumerate(words):
        response = re.sub(word, words[-i-1], st)

    return response


