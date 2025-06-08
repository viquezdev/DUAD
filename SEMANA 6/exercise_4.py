#4. Cree una función que le de la vuelta a un string y lo retorne.
 #   1. Esto ya lo hicimos en iterables.
 #   2. “Hola mundo” → “odnum aloH”


def reverse_string(my_string):
    letter=""
    for index in range(len(my_string)-1,-1,-1):
        letter+=my_string[index]
        
    return letter
	
print(reverse_string('Pizza con piña'))