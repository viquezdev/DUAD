my_list = [4, 3, 6, 1, 7]
first_element=my_list.pop(0)
last_element=my_list.pop()
my_list.insert(0,last_element)
my_list.insert(len(my_list),first_element)
print(my_list)