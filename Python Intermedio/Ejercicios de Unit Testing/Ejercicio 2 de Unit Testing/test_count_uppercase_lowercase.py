from Ejer_5_fun_count_uppercase_lowercase import count_uppercase_lowercase

def test_count_uppercase_lowercase():
    #Arrange
    my_string = "I love Nación Sushi"
    #Act  
    result = count_uppercase_lowercase(my_string)  
    #Assert
    assert result == " Theres 3 upper cases and 13 lower cases "

def test_count_uppercase_lowercase_with_numbers_and_special_characters():
    #Arrange
    my_string = "12345"
    #Act
    result = count_uppercase_lowercase(my_string)
    #Assert
    assert result == " Theres 0 upper cases and 0 lower cases "

def test_count_uppercase_lowercase_with_empty_string():
    #Arrange        
    my_string = ""
    #Act
    result = count_uppercase_lowercase(my_string)
    #Assert
    assert result == " Theres 0 upper cases and 0 lower cases "