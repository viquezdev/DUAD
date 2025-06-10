#me di cuenta que si hago el recorrido en orden se brinca numeros
#por lo que tuve que hacer el recorrido de atras hacia adelante
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for index in range(len(my_list)-1,-1,-1):
	if(my_list[index]%2!=0):
		my_list.pop(index)
print(my_list)