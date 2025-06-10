#3. Cree una función que retorne la suma de todos los números de una lista.
 #   1. La función va a tener un parámetro (la lista) y retornar un numero (la suma de todos sus elementos).
  #  2. [4, 6, 2, 29] → 41


def sum_of_list(list):
    total_sum=0
    for number in list:
        total_sum+=number
    return total_sum

print(sum_of_list([4,6,2,29]))