


def reverse_string(my_string):
    letter=""
    for index in range(len(my_string)-1,-1,-1):
        letter+=my_string[index]
        
    return letter
	
print(reverse_string('Pizza con piña'))