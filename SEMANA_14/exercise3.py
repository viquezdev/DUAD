#Cree una estructura de objetos que asemeje un Binary Tree.


class Node:
    data: str
    left: "Node"
    right: "Node"

    def __init__(self, data, left=None,right=None):
        self.data = data
        self.left= left
        self.right=right


class BinaryTree:
    root: Node


    def __init__(self, root=None):
        self.root = root
    

    def print_structure(self,node=None):
        if node is None:
            return
        print(node.data)
        self.print_structure(node.left) 
        self.print_structure(node.right)

        
    def add_node(self, new_node,current_node=None):
        if self.root is None:
            self.root = new_node
            return True
        
        if current_node is None:
            current_node=self.root

        if current_node.left is None:
            current_node.left=new_node
            return True
        
        elif current_node.right is None:
            current_node.right=new_node
            return True
        else:
            if self.add_node(new_node,current_node.left):
                return True
            return self.add_node(new_node,current_node.right)                 




node_a=Node('A')
node_b=Node('B')
node_c=Node('C')
node_d=Node('D')
node_e=Node('E')
node_f=Node('F')
node_g=Node('G')
my_binary_tree=BinaryTree()
my_binary_tree.add_node(node_a)
my_binary_tree.add_node(node_b)
my_binary_tree.add_node(node_c)
my_binary_tree.add_node(node_d)
my_binary_tree.add_node(node_e)
my_binary_tree.add_node(node_f)
my_binary_tree.add_node(node_g)
my_binary_tree.print_structure(my_binary_tree.root)