from reverse_string import reverse_string


def test_reverse_string_regular_input():
    #Arrange
    text='Pizza con piña'
    #Act
    result=reverse_string(text)
    #Assert
    assert result=="añip noc azziP"


def test_reverse_string_empty_input():
    #Arrange
    text=''
    #Act
    result=reverse_string(text)
    #Assert
    assert result==""


def test_reverse_string_no_spaces():
    #Arrange
    text='Pizzaconpiña'
    #Act
    result=reverse_string(text)
    #Assert
    assert result=="añipnocazziP"



