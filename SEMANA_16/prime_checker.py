def if_prime(number):
    counter=1
    counter_prime=0
    while(counter<=number):
        if(number%counter==0):
            counter_prime+=1
        counter+=1
        
    if(counter_prime==2):
        return number
    else:
        return 0


def get_prime_numbers(list_of_numbers):
    new_list=[]
    for number in list_of_numbers:
        if(if_prime(number)!=0):
            new_list.append(number)
    return(new_list)


print(get_prime_numbers([1, 4, 6, 7, 13, 9, 67]))

print(if_prime(1))