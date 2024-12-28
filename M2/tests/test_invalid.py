def test_invalid(reconstruct):
    result = reconstruct("qwertyuiopzxcvbnm")
    assert result is None
