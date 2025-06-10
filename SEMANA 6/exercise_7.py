#Cree una función que acepte una lista de números y retorne una lista con los números primos de la misma.
#1. [1, 4, 6, 7, 13, 9, 67] → [7, 13, 67]
#2. Tip 1: Investigue la logica matematica para averiguar si un numero es primo, y conviertala a codigo. No busque el codigo, eso no ayudaria.
#3. *Tip 2: Aquí hay que hacer varias cosas (recorrer la lista, revisar si cada numero es primo, y agregarlo a otra lista). Así que lo mejor es agregar **otra función** para revisar si el numero es primo o no.*


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