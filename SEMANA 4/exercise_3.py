import random

secret_number=random.randint(1,10)
user_input_number=0
while(secret_number!=user_input_number):
    user_input_number=int(input("Tell me a number between 1 and 10: "))
print("you won")
