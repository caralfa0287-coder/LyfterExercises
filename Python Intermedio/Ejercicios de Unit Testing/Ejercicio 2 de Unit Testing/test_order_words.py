from Ejer_6_fun_order_words import order_words

def test_order_words():
    #Arrange
    input_word = 'python-variable-funcion-computadora-monitor'
    expected_output = 'computadora-funcion-monitor-python-variable' 
    #Act
    result = order_words(input_word)
    #Assert
    assert result == expected_output

def test_order_words_with_empty_string():
    #Arrange
    input_word = ''
    expected_output = '' 
    #Act
    result = order_words(input_word)
    #Assert
    assert result == expected_output

def test_order_words_with_dot_separated_words():
    #Arrange
    input_word = 'python.variable.funcion.computadora.monitor'
    expected_output = 'computadora-funcion-monitor-python-variable' 
    #Act
    result = order_words(input_word.replace('.', '-'))
    #Assert
    assert result == expected_output