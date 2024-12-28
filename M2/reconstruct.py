from math import inf, log
from typing import List, Optional

from utils import max_word_length, is_valid, word_prob

# Part A: Naive reconstruction

def naive_reconstruct(document: str) -> Optional[str]:
    """
    Finds any valid reconstruction of a string with no whitespace.
    :param document: A nonempty string with no whitespace.
    :return: A reconstruction of the string, with spaces (no added punctuation),
    or None if it does not form a sequence of valid dictionary words.
    """
    word = ''
    reconstruct = ''
    if len(document.split()) > 1:
        raise ValueError('Document must not contain any whitespace.')
    for l in document:
        word+=l
        if is_valid(word):
            reconstruct += word + " "
            word = ''
    if(reconstruct == ''):
        return None
    else:
        return reconstruct 
    # todo


def backtrack(document: str, indices: List[Optional[int]]) -> str:
    """
    :param document: A nonempty string of n letters,
    stripped of all whitespace and punctuation.
    :param indices: A list of length (n+1) used for backtracking.
    If the first i characters of document form a valid sequence of words,
    then indices [i] contains the starting index of the last word.
    Otherwise, if document[:i+1] is invalid, indices[i] contains None.
    If document[:i+1] forms a valid sequence of words, then indices[i] contains
    the starting index of the last word, or None if document[:i+1] is invalid.
    :return: The reconstructed document, with spaces between words.
    >>> backtrack("xylophoneplayer", [None, None, None, 0, 0, 3, 3, 4, 4, 0, 7, 8, 9, 9, 9, 9])
    'xylophone player'
    """
    assert indices[-1] is not None
    # todo

    result = []
    i = len(document)
    while i > 0:
        if indices[i] is None:
            return "Invalid reconstruction"
        j = indices[i]
        result.append(document[j:i])
        i = j
    print(' '.join(reversed(result)))
    return ' '.join(reversed(result))

    

    # note: Repeated string concatenation (with + or +=) can be inefficient in some circumstances,
    # since it requires Python to copy the same characters many time.
    # Consider using the string `join` method instead.


# Part B: Probabilistic reconstruction

def likely_reconstruct(document: str) -> Optional[str]:
    """
    Finds the **most likely** reconstruction of a string with no whitespace.
    :param document: A nonempty string of letters, stripped of all whitespace
    and punctuation.
    :return: A string which is the most likely reconstruction of the input,
    or None if all reconstructions have zero probability.
    """
    if len(document.split()) > 1:
        raise ValueError('Document must not contain any whitespace.')
    # todo

    n = len(document)
    DP = [float('inf')] * (n + 1)    # Initialize DP table
    indices = [None] * (n + 1)
    DP[0] = 0   # Base case

    for i in range(1, n + 1):
        for j in range(i):
            word = document[j:i]
            if is_valid(word):
                p = -log(word_prob(word))
                if DP[j] + p < DP[i]:
                    DP[i] = DP[j] + p
                    indices[i] = j
                

    if DP[n] == float('inf'):
        return None

    return backtrack(document, indices)


if __name__ == "__main__":
    # You can manually test your code here
    result = likely_reconstruct("applecider")
    print(result)
    print(result.split(' '))
    #pass
