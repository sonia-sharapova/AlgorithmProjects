import pytest
from typing import List, Optional

from reconstruct import backtrack


@pytest.mark.slow
def test_backtrack():
    sentence = 'algorithm is an anagram of logarithm'
    orig_indices = [0] + [i+1 for i, c in enumerate(sentence) if c == ' ']
    stripped_indices = [idx - j for j, idx in enumerate(orig_indices)]
    s = sentence.replace(' ', '')
    indices: List[Optional[int]] = [None] * (len(s) + 1)
    for i, j in zip(stripped_indices, stripped_indices[1:]):
        indices[j] = i
    indices[-1] = stripped_indices[-1]
    assert backtrack(sentence.replace(' ', ''), indices) == sentence
