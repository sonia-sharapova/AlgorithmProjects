from utils import random_combination_with_replacement, dictionary
from tests.utils import is_valid_word_sequence


def test_random_100000(reconstruct):
    s = ' '.join(random_combination_with_replacement(dictionary, 10 ** 5))
    result = reconstruct(s.replace(' ', ''))
    assert is_valid_word_sequence(result.split(' '))
