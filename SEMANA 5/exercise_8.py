key_list = ['access_level', 'age']
employee_data = {'employee_name': 'Juan', 'email': 'john@ecorp.com', 'access_level': 5, 'age': 28}

for key in key_list:
    employee_data.pop(key)         
print(employee_data)