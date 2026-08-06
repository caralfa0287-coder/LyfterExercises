from Ejer_7_fun_is_prime_number import filter_prime

def test_is_prime_number_with_a_list_of_numbers():
    #Arrange
    n = [1, 4, 6, 7, 13, 9, 67 ]
    #Act
    result = filter_prime(n)
    #Assert
    assert result == [7, 13, 67]

def test_is_prime_number_with_non_prime_numbers():
    #Arrange
    n = [8, 10, 12, 15, 20]
    #Act
    result = filter_prime(n)
    #Assert
    assert result == []

def test_is_prime_number_with_big_numbers():
    #Arrange
    n = [11113, 234579, 309933, 412377, 10000019]
    #Act
    result = filter_prime(n)
    #Assert
    assert result == [11113, 10000019]