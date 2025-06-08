
new_dictionary={}
list_a = ['first_name', 'last_name', 'employee_role']
list_b = ['Alek', 'Castillo', 'Software Engineer']
for index in range(0,len(list_a)):
    new_dictionary[list_a[index]]=list_b[index]
print(new_dictionary)