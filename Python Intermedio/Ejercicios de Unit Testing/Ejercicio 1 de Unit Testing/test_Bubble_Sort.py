import pytest
from Bubble_Sort import validated_bubble_sort

def test_validated_bubble_sort_with_small_list_returns_correctly_sorted_test():
    # Arrange
    list_input = [64, 34, 25, 12, 22, 11, 90]
    # Act
    result = validated_bubble_sort(list_input)
    # Assert
    assert result == [11, 12, 22, 25, 34, 64, 90]


def test_validated_bubble_sort_with_big_list_returns_correctly_sorted_test1():
    # Arrange
    list_input = [
    45, 62, 89, 3, 56, 78, 23, 90, 11, 34, 
    67, 82, 19, 4, 55, 33, 99, 8, 72, 
    41, 15, 60, 27, 88, 5, 39, 94, 16, 50, 
    73, 2, 84, 29, 61, 44, 9, 79, 31, 97, 
    18, 54, 81, 26, 68, 14, 92, 36, 70, 48, 
    22, 85, 7, 43, 91, 13, 58, 25, 77, 35, 
    95, 10, 52, 80, 24, 69, 38, 87, 1, 63, 
    47, 20, 75, 42, 98, 17, 59, 28, 83, 32, 
    96, 6, 51, 76, 30, 65, 49, 86, 21, 64, 
    46, 37, 74, 53, 93, 12, 66, 40, 71, 57,
    101, 103, 100, 102
]

    # Act
    result = validated_bubble_sort(list_input)
    # Assert
    assert result == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 
                    11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 
                    21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 
                    31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 
                    41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 
                    51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 
                    61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 
                    71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 
                    81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 
                    91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 
                    101, 102, 103
                    ]


def test_validated_bubble_sort_with_non_list_input_returns_type_error():
    # Arrange
    list_input = "not a list"
    # Act & Assert
    with pytest.raises(TypeError, match="Error: La entrada debe ser una lista numérica"):
        validated_bubble_sort(list_input)

def test_validated_bubble_sort_with_empty_list_returns_empty_list():
    # Arrange
    list_input = []
    # Act
    result = validated_bubble_sort(list_input)
    # Assert    
    assert result == []  # The function should return an empty list without raising an error
    


