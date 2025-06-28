class Node:
    data: int
    next: "Node"

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:
    head: Node

    def __init__(self, head):
        self.head = head

    def print_structure(self):
        current_node = self.head

        while (current_node is not None):
            print(current_node.data)
            current_node = current_node.next

    def count_nodes(self):
        current_node=self.head
        count=0
        while(current_node!=None):
            count+=1
            current_node=current_node.next
        return count

    def BubbleSort(self):
        current_element=self.head
        for other_index in range(0,(self.count_nodes())-1):
            for index in range(0, (self.count_nodes())-1-other_index):
                
                has_made_changes=False
                data=current_element.data
                next_element=current_element.next

                if(current_element.data>next_element.data):
                    current_element.data=next_element.data
                    current_element.next.data=data
                    has_made_changes=True
                
                current_element=current_element.next

            current_element=self.head
        if not has_made_changes:
            return

seventh_node=Node(-2)
sixth_node_node=Node(53,seventh_node)
fifth_node=Node(32,sixth_node_node)
fourth_node=Node(6,fifth_node)
third_node = Node(68,fourth_node)
second_node = Node(-11, third_node)
first_node = Node(18, second_node)

linked_list = LinkedList(first_node)
linked_list.BubbleSort()
linked_list.print_structure()


