import pytest
from bubble_sort import bubble_sort


def test_bubble_sort_with_small_list():
    #Arrange
    small_list=[-5,45,98,21,-2,56]
    #Act
    result=bubble_sort(small_list)
    #Assert
    assert result==small_list.sort()


def test_bubble_sort_with_big_list():
    #Arrange
    big_list=numbers = [
    23, -15, 42, -8, 0, -99, 77, -34, 18, 3,
    -56, 88, -2, 14, -67, 35, -1, 60, -30, 91,
    -45, 7, -12, 100, -77, 5, -9, 27, -22, 50,
    -18, 36, -25, 73, -3, 11, -6, 64, -40, 85,
    -72, 2, -20, 46, -11, 9, -60, 80, -10, 1
    ]
    #Act
    result=bubble_sort(big_list)
    #Assert
    assert result==big_list.sort()

#UnboundLocalError: cannot access local variable 'has_made_changes' where it is not associated with a value
def test_bubble_sort_with_empty_list():
    #Arrange
    empty_list=[]
    #Act
    result=bubble_sort(empty_list)
    #Assert
    assert result==empty_list.sort()


#Failed: DID NOT RAISE <class 'TypeError'>
def test_bubble_sort_with_invalid_input():
    #Arrange
    other_param='hola'
    #Act & Assert
    with pytest.raises(TypeError):
        bubble_sort(other_param)