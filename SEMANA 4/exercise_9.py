sum_total=0
counter=1
target_number=0
while(counter<=3):
    number=int(input("Tell me a number: "))
    sum_total=sum_total+number
    counter+=1
    if(number==30):
        target_number=1

if(sum_total==30 or target_number==1):
    print("Correct!")
else:
    print("Incorrect!")
     