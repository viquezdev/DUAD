

def bubble_sort(list_to_sort):
    for outer_index in range(0,len(list_to_sort)-1) :   
        for index in range(0,len(list_to_sort)-1-outer_index):
            has_made_changes=False
            current_element=list_to_sort[index]
            nex_element=list_to_sort[index+1]
            print(f'-- Iteration {index}. Current element: {current_element}, Next element: {nex_element}')


            if(current_element>nex_element):
                print('The current element is greater than the next one.Swapping them...')
                list_to_sort[index]=nex_element
                list_to_sort[index+1]=current_element
                has_made_changes= True
                

    if not has_made_changes:
        return

my_text_list=[18,-11,68,6,32,53,-2]
bubble_sort(my_text_list)

print(my_text_list)