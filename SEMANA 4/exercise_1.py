age=30
total_price=50.99

email_address="luisdaniel3113@hotmail.com"
first_name="Luis"
last_name="Víquez"

password_valid=True
is_game_over=False

colors=["red","green","blue"]
products_id=[10,11,12]

print(first_name+" "+last_name)#Luis Víquez
#print(first_name+age) #can only concatenate str (not "int") to str
print(colors+products_id)#['red', 'green', 'blue', 10, 11, 12]
#print(first_name+colors)#can only concatenate str (not "list") to str
print(age+total_price)#80.99000000000001
print(password_valid+is_game_over)#1