import pytest
from Ejer_4_fun_reversed_string import reversed_string


def test_reversed_string_with_a_simple_word():
    # Arrange
    s = "hello"
    # Act
    result = reversed_string(s)
    # Assert
    assert result == "olleh"

def test_reversed_string_with_spaces():
    # Arrange
    s = "hello world"
    # Act
    result = reversed_string(s)
    # Assert
    assert result == "dlrow olleh"

def test_reversed_string_with_special_characters():
    # Arrange
    s = "hello!@#"
    # Act
    result = reversed_string(s)
    # Assert
    assert result == "#@!olleh" 