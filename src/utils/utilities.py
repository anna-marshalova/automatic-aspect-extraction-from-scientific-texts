from typing import List

from nltk.tokenize import wordpunct_tokenize

def tokenize(text: str) -> List[str]:
    puncts = {'(', ')', ':', ';', ',', '.', '"', '»', '«', '[', ']', '{', '}', '%'}

    tokens = wordpunct_tokenize(text)
    validated_tokens = []
    for token in tokens:
        is_all_puncts = True
        for char in token:
            if char not in puncts:
                is_all_puncts = False
        if is_all_puncts:
            validated_tokens.extend(list(token))
        else:
            validated_tokens.append(token)
    return validated_tokens