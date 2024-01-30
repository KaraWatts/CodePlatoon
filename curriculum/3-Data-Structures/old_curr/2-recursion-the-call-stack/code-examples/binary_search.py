from .binary_tree import myTree


def binary_search(tree, value):
    # if we call BinarySearch on an empty tree (which we will do in recursive cases) return None
    if tree == None:
        return None

    if value == tree.value:
        return tree
    elif value < tree.value:
        return binary_search(tree.left, value)
    else:
        return binary_search(tree.right, value)


print(binary_search(myTree, 1))
