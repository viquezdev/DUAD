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
    return (f"There’s {count_upper} upper cases and {count_lower} lower cases")


print(count_upper_and_lower("Br1ght!Skie$ run4Ever@ Night#FloweR$ 7rain^Walk"))