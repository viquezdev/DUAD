

def bubble_sort(list_to_sort):
    for other_index in range(0,len(list_to_sort)-1): # O(n)
        for index in range(0, len(list_to_sort)-1-other_index):  # O(n^2)
            has_made_changes=False # O(1)
            current_element=list_to_sort[index] # O(1)
            next_element=list_to_sort[index+1] # O(1)

            if(current_element>next_element): # O(1)
                list_to_sort[index]=next_element # O(1)
                list_to_sort[index+1]=current_element # O(1)
                has_made_changes=True # O(1)

    if not has_made_changes: # O(1)
        return # O(1)

my_list=[-5,45,98,21,-2,56] # O(1)
bubble_sort(my_list) #  O(n^2)
print(my_list) # O(n)