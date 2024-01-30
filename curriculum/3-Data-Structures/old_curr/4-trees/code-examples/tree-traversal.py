from .binary_tree import myTree

# find an element in a tree and if found
# return the subtree of the matching node

# recursively search for value


def find_in_tree(tree, target):
    # base case, 'no tree' (child of leaf), return None
    if tree == None:
        return None

    # if at this level, return (whole tree)
    if tree.value == target:
        return tree

    # if not, search the children
    found_left = find_in_tree(tree.left, target)
    found_right = find_in_tree(tree.right, target)

    if found_left:
        return found_left
    elif found_right:
        return found_right
    else:
        return None


# print(find_in_tree(myTree, 56))
# print(find_in_tree(myTree, 22))
# print(find_in_tree(myTree, 77))
# print(find_in_tree(myTree, 1000))
