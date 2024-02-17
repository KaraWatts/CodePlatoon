
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return f"{self.value}"
    
class BinaryTree:
    def __init__(self):
        self.root = None
    
    def insert(self, new_node):
        if self.root is None:
            self.root = new_node
        else:
            self.insert_node(self.root, new_node)
        
    def __repr__(self):
        return f"{self.root}"

    def insert_node(self, current_node, new_node):
        if new_node.value <= current_node.value:
            if current_node.left:
                self.insert_node(current_node.left, new_node)
            else:
                current_node.left = new_node
        elif new_node.value > current_node.value:
            if current_node.right:
                self.insert_node(current_node.right, new_node)
            else:
                current_node.right = new_node

    # find_smallest goes here
     # Recursively
    def find_smallest(self, node = None):
        if not node:
            current = self.root
        else:
            current = node

        if not current.left:
            return current.value
        
        if not current.right or current.left.value < current.right.value:
            return self.find_smallest(current.left)
  


# node1 = Node(5)
# node2 = Node(4)
# node3 = Node(10)
# node4 = Node(2)
# node5 = Node(7)
# node6 = Node(6)
# node7 = Node(8)
# tree = BinaryTree()
# tree.insert(node1)
# tree.insert(node7)
# tree.insert(node2)
# tree.insert(node3)
# tree.insert(node4)
# tree.insert(node5)
# tree.insert(node6)


# # As a while loop   
# def find_smallest_while(current):

#     while current.left:
#         if not current.right or current.left.value < current.right.value:
#             current = current.left
#         else:
#             current = current.right

#     return(current)


# # Recursively
# def find_smallest(current_node):
#     try:
#         current = current_node.root
#     except:
#         current = current_node
#     if not current.left:
#         return current
    
#     if not current.right or current.left.value < current.right.value:
#         return find_smallest(current.left)
#     else:
#         return find_smallest(current.right)

# print(find_smallest(tree))