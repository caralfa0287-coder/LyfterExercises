import pytest
from Ejer_3_fun_sum_number_list import sum_number_list

def test_sum_number_list_with_positive_numbers():
    # Arrange
    numbers = [1, 2, 3, 4, 5]
    # Act
    result = sum_number_list(numbers)
    # Assert
    assert result == 15

def test_sum_number_list_with_negative_numbers():
    # Arrange
    numbers = [-1, -2, -3, -4, -5]
    # Act
    result = sum_number_list(numbers)
    # Assert
    assert result == -15

def test_sum_number_list_with_mixed_numbers():
    # Arrange
    numbers = [-1, 2, -3, 4, -5]
    # Act
    result = sum_number_list(numbers)
    # Assert
    assert result == -3
