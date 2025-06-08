#range(start, stop, step)
#start	Optional. An integer number specifying at which position to start. Default is 0
#stop	Required. An integer number specifying at which position to stop (not included).
#step	Optional. An integer number specifying the incrementation. Default is 1

my_string = 'Pizza con piña'

for index in range(len(my_string)-1,-1,-1):
	letter=my_string[index]
	print(f"{letter}")
