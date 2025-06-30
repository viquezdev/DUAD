from alphabetical_sort import ordered_text


def test_ordered_text_with_multiple_words():
    #Arrange
    text="python-variable-function-computer-monitor"
    #Act
    result=ordered_text(text)
    #Assert
    assert result==['computer', 'function', 'monitor', 'python', 'variable']


def test_ordered_text_with_empty_string():
    #Arrange
    text=" "
    #Act
    result=ordered_text(text)
    #Assert
    assert result==[' ']


#AssertionError: assert ['COMPUTER', ...or', 'python'] == ['COMPUTER', ...', 'VARIABLE']
def test_ordered_text_with_mixed_case():
    #Arrange
    text="python-VARIABLE-function-COMPUTER-monitor"
    #Act
    result=ordered_text(text)
    #Assert
    assert result==['COMPUTER', 'function', 'monitor', 'python', 'VARIABLE']



