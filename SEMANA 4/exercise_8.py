number=int(input("Tell me a number: "))
if(number%3==0 and number%5==0):
    print("FizzBuzz")
else:
    if(number%3==0):
        print("Fizz")
    else:
        if(number%5==0):
            print("Buzz")