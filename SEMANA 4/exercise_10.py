time_in_seconds=int(input("Enter the time in seconds: "))
minutes=time_in_seconds//60
if(minutes<10):
    print(600-time_in_seconds)
else:
    if(minutes>10):
        print("Mayor")
    else:
        print("igual")