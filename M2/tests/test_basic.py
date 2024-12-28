from tests.utils import is_valid_word_sequence


def test_basic(reconstruct):
    stripped = 'applecider'
    result = reconstruct(stripped)
    assert is_valid_word_sequence(result.split(' '))
