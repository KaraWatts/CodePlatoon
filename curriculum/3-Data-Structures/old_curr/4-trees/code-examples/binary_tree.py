class BinaryTree:
    def __init__(self, value, left=None, right=None):
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


# Notice the substructure
myTree = BinaryTree(
    56,
    BinaryTree(
        22,
        BinaryTree(10),
        BinaryTree(30)
    ),
    BinaryTree(
        81,
        BinaryTree(77),
        BinaryTree(92)
    )
)
