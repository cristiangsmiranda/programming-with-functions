import pytest
from counting_words import counting_words

@pytest.mark.parametrize("filename, word, expected_count, expected_lines", [
    ("Joseph_history.txt", "Vermont", 2, [11, 12]),
    ("Joseph_history.txt", "Church", 6, [2, 4, 6, 7, 9, 34]),
    ("Joseph_history.txt", "nonexistentword", 0, [])
])
def test_counting_words(filename, word, expected_count, expected_lines):
    count, lines = counting_words(filename, word)
    assert count == expected_count
    assert lines == expected_lines

if __name__ == "__main__":
    pytest.main(["-v", "--maxfail=1", "test_counting_word.py"])
