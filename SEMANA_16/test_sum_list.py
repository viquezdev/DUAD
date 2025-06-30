import pytest
from sum_list import sum_of_list


def test_sum_of_list_sum_all_elements():
    #Arrange
    number_list=[5,6,8,12,34]
    #Act
    result=sum_of_list(number_list)
    #Assert
    assert result==65


def test_sum_of_list_empty_list():
    #Arrange
    number_list=[]
    #Act
    result=sum_of_list(number_list)
    #Assert
    assert result==0


def test_sum_of_list_throws_exception_with_string():
    #Arrange
    number_list=['5',6,8,12,34]
    # Act & Assert
    with pytest.raises(TypeError):
        sum_of_list(number_list)

