largest_number=0
counter=1
while(counter<=100):
    counter+=1
    number=int(input("Tell me a number: "))
    if(number>largest_number):
        largest_number=number
print(f"The largest number is {largest_number}")