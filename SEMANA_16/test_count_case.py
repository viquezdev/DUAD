from count_case import count_upper_and_lower


def test_count_upper_and_lower_regular_input():
    #Arrange
    text="I love Nación Sushi"
    #Act
    result=count_upper_and_lower(text)
    #Assert
    assert result=="There’s 3 upper cases and 13 lower cases"


#ssertionError: assert 'There’s 7 up...7 lower cases' == 'There’s 7 up...8 lower cases'
def test_count_upper_and_lower_with_numbers_and_symbols():
    #Arrange
    text="Br1ght!Skie$ run4Ever@ Night#FloweR$ 7rain^Walk"
    #Act
    result=count_upper_and_lower(text)
    #Assert
    assert result=="There’s 7 upper cases and 28 lower cases"


def test_count_upper_and_lower_empty_input():
    #Arrange
    text=""
    #Act
    result=count_upper_and_lower(text)
    #Assert
    assert result=="There’s 0 upper cases and 0 lower cases"