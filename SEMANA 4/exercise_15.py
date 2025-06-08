total_count=1
male_count=0
female_count=0
male_percentage=0
female_percentage=0
while(total_count<=6):
    gender=input("Enter M if the person is male or F if the person is female: ")
    if(gender=="M"):
        male_count+=1
    else:
        female_count+=1
    total_count+=1
male_percentage=(male_count/6)*100
female_percentage=(female_count/6)*100
print(f"The percentage of males is {male_percentage}")
print(f"The percentage of females is {female_percentage}")