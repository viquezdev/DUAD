#Cree una estructura de objetos que asemeje un Stack.


class Node:
    data: str
    next: "Node"

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Stack:
    top: Node

    def __init__(self, top):
        self.top = top


    def print_structure(self):
        current_node = self.top
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next


    def push(self, new_node):
        if self.top is None:
            self.top = new_node
            return
        current_node = self.top
        self.top=new_node
        self.top.next=current_node
        

    def pop(self):
        if self.top:
            self.top = self.top.next


first_node = Node("Hello")
my_stack = Stack(first_node)


second_node = Node("World")
my_stack.push(second_node)


third_node= Node("Third")
my_stack.push(third_node)

my_stack.print_structure()

print("POP")
my_stack.pop()
my_stack.print_structure()

print("PUSH")
forth_node= Node("Forth")
my_stack.push(forth_node)
my_stack.print_structure()

