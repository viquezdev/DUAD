

def bubble_sort(list_to_sort):
    for other_index in range(len(list_to_sort)-1,0,-1):
        for index in range(len(list_to_sort)-1,0,-1):
            has_made_changes=False
            current_element=list_to_sort[index]
            next_element=list_to_sort[index-1]

            if(current_element<next_element):
                list_to_sort[index]=next_element
                list_to_sort[index-1]=current_element
                has_made_changes=True
                

    if not has_made_changes:
        return

my_list=[9,8,7,6,5,4,3,2,1]
bubble_sort(my_list)
print(my_list)