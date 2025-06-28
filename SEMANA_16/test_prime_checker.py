import pytest
from prime_checker import *


def test_if_prime_with_string_input():
    #Arrange
    number='45'
    #Act & Assert
    with pytest.raises(TypeError):
        if_prime(number)

    
def test_if_prime_with_negative_number():
    #Arrange
    number=-3
    #Act 
    result=if_prime(number)
    #Assert
    assert result==0


def test_if_prime_with_one():
    #Arrange
    number=1
    #Act 
    result=if_prime(number)
    #Assert
    assert result==0


def test_get_prime_numbers_with_empty_list():
    #Arrange
    list_of_numbers=[]
    #Act 
    result=list_of_numbers
    #Assert
    assert result==[]


def test_get_prime_numbers_with_strings():
    #Arrange
    list_of_numbers=['1','2','3']
    #Act & assert
    with pytest.raises(TypeError):
        get_prime_numbers(list_of_numbers)

