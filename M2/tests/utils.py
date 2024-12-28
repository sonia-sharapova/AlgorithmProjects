from reconstruct import is_valid


def is_valid_word_sequence(words):
    return all(is_valid(w) for w in words)
