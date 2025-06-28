def bubble_sort(list_to_sort):
    if list_to_sort==[]:
        return
    if not isinstance(list_to_sort,list):
        return
    for other_index in range(0,len(list_to_sort)-1):
        for index in range(0, len(list_to_sort)-1-other_index):
            has_made_changes=False
            current_element=list_to_sort[index]
            next_element=list_to_sort[index+1]

            if(current_element>next_element):
                list_to_sort[index]=next_element
                list_to_sort[index+1]=current_element
                has_made_changes=True

    if not has_made_changes:
        return

my_list=[]
bubble_sort(my_list)
print(my_list)