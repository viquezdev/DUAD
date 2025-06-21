#Cree una estructura de objetos que asemeje un Double Ended Queue


class Node:
    data: str
    next: "Node"

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class DoubleEndedQueue:
    head: Node
    tail: Node

    def __init__(self, head,tail):
        self.head = head
        self.tail=tail


    def print_structure(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next


    def push_left(self, new_node):
        if (self.head is None) and (self.tail is None):
            self.head = new_node
            self.tail= new_node
            return
        current_node = self.head
        self.head=new_node
        self.head.next=current_node


    def push_right(self, new_node):
        if (self.head is None) and (self.tail is None):
            self.head = new_node
            self.tail= new_node
            return
        current_node = self.tail
        self.tail=new_node
        current_node.next=self.tail
        

    def pop_left(self):
        if self.head:
            self.head = self.head.next

    def pop_right(self):
        if self.head:
            current_node = self.head
            while current_node.next is not self.tail:
                current_node = current_node.next

        self.tail=current_node
        self.tail.next=None


first_node = Node("First")
my_double_ended_queue=DoubleEndedQueue(first_node,first_node)


second_node = Node("Second")
my_double_ended_queue.push_left(second_node)


third_node= Node("Third")
my_double_ended_queue.push_right(third_node)


forth_node= Node("Forth")
my_double_ended_queue.push_left(forth_node)

my_double_ended_queue.print_structure()


print("POP LEFT")
my_double_ended_queue.pop_left()
my_double_ended_queue.print_structure()

print("POP RIGHT")
my_double_ended_queue.pop_right()
my_double_ended_queue.print_structure()

print("POP RIGHT")
my_double_ended_queue.pop_right()
my_double_ended_queue.print_structure()

print("POP LEFT")
my_double_ended_queue.pop_left()
my_double_ended_queue.print_structure()

fifth_node= Node("fifth")
my_double_ended_queue.push_left(fifth_node)

my_double_ended_queue.print_structure()