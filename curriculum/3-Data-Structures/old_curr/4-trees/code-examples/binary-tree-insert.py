"""Binary Search Tree"""


class BinaryTree:
    """binary tree"""
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    # even printing the tree requires a recursive approach
    def __str__(self, level=0):
        def leaf_str():
            return '\t' * (level+1) + 'None\n'

        tree_str = '\t' * level + repr(self.value) + '\n'

        for child in [self.left, self.right]:
            tree_str += child.__str__(level+1) if child else leaf_str()

        return tree_str


def binary_tree_insert(tree, new_value):
    """ 
    Sorted insert of integers into a binary tree. Returns the tree (i.e. returns root node).
    It uses recursion and passes in child nodes of the tree as their own little subtrees.
    """

    if tree is None:
        print("empty tree, creating root node")
        return BinaryTree(new_value)

    # left
    if new_value < tree.value:
        print(f"new_val {new_value} < {tree.value}, going to left")

        # base case
        if tree.left is None:
            print("new left node")
            tree.left = BinaryTree(new_value)
        # recurse
        else:
            binary_tree_insert(tree.left, new_value)
    
    # right
    else:
        print(f"new_val {new_value} >= {tree.value}, going to right")
        # base case
        if tree.right is None:
            print("new right node")
            tree.right = BinaryTree(new_value)
        # recurse
        else:
            binary_tree_insert(tree.right, new_value)

    return tree

# inserting some stuff into our tree
my_tree = binary_tree_insert(None, 50)
print(my_tree.value) # 50

my_tree = binary_tree_insert(my_tree, 25)
print(my_tree.left.value) # 25

my_tree = binary_tree_insert(my_tree, 75)
print(my_tree.right.value) # 75

my_tree = binary_tree_insert(my_tree, 10)
print(my_tree.left.value) # 25
print(my_tree.left.left.value) # 10


my_tree = binary_tree_insert(my_tree, 1)
print(my_tree.left.left.left.value) # 1

my_tree = binary_tree_insert(my_tree, 100)
print(my_tree.right.right.value) # 100