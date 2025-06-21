#Cree una estructura de objetos que asemeje un Binary Tree.


class Node:
    data: str
    next: "Node"

    def __init__(self, data, left_next=None,right_next=None):
        self.data = data
        self.left_next = left_next
        self.right_next=right_next


class BinaryTree:
    root: Node


    def __init__(self, root):
        self.root = root
    

    def print_structure(self,node=None):
        if node is None:
            return
        
        print(node.data)
        self.print_structure(node.left_next)
        self.print_structure(node.right_next)

        
    def add_node(self, new_node):
        if (self.root is None):
            self.root = new_node
            return
        current_node = self.root
        while (current_node.left_next is not None) and (current_node.right_next is not None):
            current_node=current_node.left_next
            if (current_node.left_next)!=None and (current_node.right_next!=None):
                current_node=self.root
                current_node=current_node.right_next
            

        if (current_node.left_next==None):
            current_node.left_next = new_node
        else:
            current_node.right_next=new_node


node_a=Node('A')
node_b=Node('B')
node_c=Node('C')
node_d=Node('D')
node_e=Node('E')
node_f=Node('F')
node_g=Node('G')
my_binary_tree=BinaryTree(node_a)
my_binary_tree.add_node(node_b)
my_binary_tree.add_node(node_c)
my_binary_tree.add_node(node_d)
my_binary_tree.add_node(node_e)
my_binary_tree.add_node(node_f)
my_binary_tree.add_node(node_g)
my_binary_tree.print_structure(my_binary_tree.root)