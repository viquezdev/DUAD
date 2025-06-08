highest_number=0
counter=1
user_input_number=0
while(counter<=3):
    counter=counter+1
    user_input_number=int(input("Tell me a number:"))
    if(user_input_number>highest_number):
        highest_number=user_input_number
print(f"The highest number is: {highest_number}")