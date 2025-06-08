counter=1
my_other_list=[]
largest_number=0
while(counter<=10):
	selected_number=int(input("Tell me a number: "))
	my_other_list.append(selected_number)
	if(selected_number>largest_number):
		largest_number=selected_number
	counter+=1
print(f"{my_other_list}. El más alto fue {largest_number}")