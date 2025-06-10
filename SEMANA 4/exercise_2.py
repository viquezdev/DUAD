first_name=input("Tell me your first name:")
last_name=input("Tell me your last name:")
age=int(input("Tell me your age:"))
if (age==0 or age==1):
    print("baby")
elif (age>1 and age<=10):
    print("child")
elif (age>10 and age<=12):
    print("preteen") 
elif (age>12 and age<=19):
    print("teenager")
elif (age>19 and age<=25):
    print("young adult")
elif (age>25 and age<=65):
    print("adult")
else:
    print("senior")