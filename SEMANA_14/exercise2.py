#Cree una estructura de objetos que asemeje un Double Ended Queue


class Node:
    data: str
    next: "Node"
    prev: "Node"

    def __init__(self, data,next=None,prev=None):
        self.data = data
        self.next = next
        self.prev= prev


class DoubleEndedQueue:
    head: Node
    tail: Node

    def __init__(self):
        self.head = None
        self.tail=None


    def print_structure(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next


    def push_left(self, new_node):
        if self.head is None:
            self.head = new_node
            self.tail= new_node
            return
        new_node.next=self.head
        self.head.prev=new_node
        self.head=new_node


    def push_right(self, new_node):
        if self.tail is None:
            self.head = new_node
            self.tail= new_node
            return
        new_node.prev=self.tail
        self.tail.next=new_node
        self.tail=new_node


    def pop_left(self):
        if self.head is None:
            print("The dequeue es empty")
        elif self.head==self.tail:
            self.head = None
            self.tail=None
        else:
            self.head=self.head.next
            self.head.prev=None

    def pop_right(self):
        if self.tail is None:
            print("The dequeue es empty")
        elif self.head==self.tail:
            self.head = None
            self.tail=None
        else:
            self.tail=self.tail.prev
            self.tail.next=None


first_node = Node("First")
my_double_ended_queue=DoubleEndedQueue()
my_double_ended_queue.push_left(first_node)


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

my_double_ended_queue.pop_left()
my_double_ended_queue.pop_right()