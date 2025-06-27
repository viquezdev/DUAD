#Cree una estructura de objetos que asemeje un Stack.


class Node:
    data: str
    next: "Node"

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Stack:
    top: Node

    def __init__(self):
        self.top = None


    def print_structure(self):
        current_node = self.top
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next


    def push(self, new_node):
        if self.top is None:
            self.top = new_node
            return
        new_node.next=self.top
        self.top=new_node



    def pop(self):
        if self.top is None:
            print("The stack is empty")
        else:
            self.top = self.top.next


first_node = Node("Hello")
my_stack = Stack()
my_stack.push(first_node)


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

my_stack.pop()
my_stack.pop()
my_stack.pop()
my_stack.pop()