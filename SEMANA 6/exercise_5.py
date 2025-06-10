#5. Cree una función que imprima el numero de mayúsculas y el numero de minúsculas en un string.
 #   1. “I love Nación Sushi” → “There’s 3 upper cases and 13 lower cases”


def count_upper_and_lower(text_to_analyze):
    count_upper=0
    count_lower=0
    for char in text_to_analyze:
        if(char==" "):
            continue
        elif(char.isupper()):
            count_upper+=1
        else:
            count_lower+=1
    print(f"There’s {count_upper} upper cases and {count_lower} lower cases")


count_upper_and_lower("I love Nación Sushi")