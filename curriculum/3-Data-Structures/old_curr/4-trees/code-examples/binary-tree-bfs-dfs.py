from collections import deque


class BinaryTree:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return f"tree w/ root: {self.val}"

    def dfs(self):
        print(self.val)
        if self.left:
            self.left.dfs()
        if self.right:
            self.right.dfs()

    def bfs(self):
        node_queue = deque()
        node_queue.append(self)

        while len(node_queue) > 0:
            current = node_queue.popleft()
            print(current.val)
            if current.left:
                node_queue.append(current.left)
            if current.right:
                node_queue.append(current.right)


tree = BinaryTree(
    1,
    BinaryTree(
        2,
        BinaryTree(4),
        BinaryTree(5)
    ),
    BinaryTree(
        3,
        BinaryTree(6),
        BinaryTree(7)
    ),
)

tree.bfs()
