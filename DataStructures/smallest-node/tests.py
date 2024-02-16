import unittest
from smallest_node import Node, BinaryTree

class TestSmallestNode(unittest.TestCase):

    def setUp(self):
        self.node1 = Node(5)
        self.node2 = Node(4)
        self.node3 = Node(10)
        self.node4 = Node(2)
        self.tree = BinaryTree()
        self.tree.insert(self.node1)
        self.tree.insert(self.node2)
        self.tree.insert(self.node3)
        self.tree.insert(self.node4)

    def test_find_smallest(self):
        self.assertEqual(self.tree.find_smallest(), 2)
    
if __name__ == "__main__":
    unittest.main()