from typing import Dict, Optional, Set
import random
import re
import string

from wordfreq import get_frequency_dict


one_letter_words = {'a', 'i'}
two_letter_scrabble_words = {
    'aa', 'ab', 'ad', 'ae', 'ag', 'ah', 'ai', 'al', 'am', 'an', 'ar', 'as',
    'at', 'aw', 'ax', 'ay', 'ba', 'be', 'bi', 'bo', 'by', 'da', 'de', 'do',
    'ed', 'ef', 'eh', 'el', 'em', 'en', 'er', 'es', 'et', 'ew', 'ex', 'fa',
    'fe', 'gi', 'go', 'ha', 'he', 'hi', 'hm', 'ho', 'id', 'if', 'in', 'is',
    'it', 'jo', 'ka', 'ji', 'la', 'li', 'lo', 'ma', 'me', 'mi', 'mm', 'mo',
    'mu', 'my', 'na', 'ne', 'no', 'nu', 'od', 'oe', 'of', 'oh', 'oi', 'ok',
    'om', 'on', 'op', 'or', 'os', 'ow', 'ox', 'oy', 'pa', 'pe', 'pi', 'po',
    'qi', 're', 'sh', 'si', 'so', 'ta', 'te', 'ti', 'to', 'uh', 'um', 'un',
    'up', 'us', 'ut', 'we', 'wo', 'xi', 'xu', 'ya', 'ye', 'yo', 'za'
}


freq = get_frequency_dict("en")
words: Set[str] = one_letter_words\
    .union(filter(lambda w: w in freq, two_letter_scrabble_words))\
    .union(set(filter(lambda w: len(w) > 2 and w == w.strip(string.punctuation).lower(), freq)))
dictionary: Dict[str, float] = {w: freq[w] for w in words}
max_word_length: int = len(max(dictionary, key=len))


def is_valid(word: str) -> bool:
    """
    Checks if a word is in the dictionary.
    Ignores case and leading or trailing punctuation.
    :param word: A nonempty string with no whitespace.
    :return True if the word is in the dictionary, and False otherwise.
    >>> is_valid("the")
    True
    >>> is_valid("end.")
    True
    >>> is_valid("en.d")
    False
    >>> is_valid("zxcvbnm")
    False
    >>> is_valid("not a word")
    Traceback (most recent call last):
    ValueError: Invalid argument: 'not a word'
    Words cannot contain whitespace
    """
    if "".join(word.split()) != word:
        raise ValueError(f"Invalid argument: '{word}'\n"
                         "Words cannot contain whitespace")
    return word.strip(string.punctuation).lower() in dictionary


def word_prob(word: str) -> float:
    """
    Computes the probability of the given word.
    Ignores case and leading or trailing punctuation.
    :param word: A nonempty string with no whitespace
    :return p: Probability that this word is chosen randomly from an English corpus.
    >>> word_prob("the")
    0.0588843655355589
    >>> word_prob("end.'")
    0.0004897788193684461
    >>> word_prob("zxcvbnm")
    0.0
    >>> word_prob("not a word")
    Traceback (most recent call last):
    ValueError: Invalid argument: not a word
    Words cannot contain whitespace
    """
    if "".join(word.split()) != word:
        raise ValueError(f"Invalid argument: {word}\n"
                         "Words cannot contain whitespace")
    w = word.strip(string.punctuation).lower()
    return dictionary[w] if w in dictionary else 0.0


def remove_whitespace(s: str) -> str:
    return re.sub(r'\s', '', s)


def remove_punctuation(s: str) -> str:
    return s.translate(str.maketrans('', '', string.punctuation))


def reconstruct_sentences(s: str, rec_fn) -> Optional[str]:
    sentences = []
    for sentence in s.split('.'):
        clauses = []
        for clause in sentence.split(','):
            if not clause:
                continue
            result = rec_fn(remove_whitespace(clause))
            if result is None:
                print(f"Could not reconstruct: '{clause}'")
                return None
            clauses.append(result)
        if clauses:
            sentences.append(', '.join(clauses))
    return ". ".join(sentences) + "."


def random_combination(iterable, r):
    """
    Random selection from itertools.combinations(iterable, r)
    """
    pool = tuple(iterable)
    n = len(pool)
    indices = sorted(random.sample(range(n), r))
    return tuple(pool[i] for i in indices)


def random_combination_with_replacement(iterable, r):
    """
    Random selection from itertools.combinations_with_replacement(iterable, r)
    """
    pool = tuple(iterable)
    n = len(pool)
    indices = sorted(random.randrange(n) for i in range(r))
    return tuple(pool[i] for i in indices)
