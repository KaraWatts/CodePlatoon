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

class TestSmallestNode2(unittest.TestCase):

    def setUp(self):
        self.node1 = Node(5)
        self.node2 = Node(4)
        self.node3 = Node(10)
        self.node4 = Node(2)
        self.node5 = Node(18)
        self.node6 = Node(7)
        self.node7 = Node(1)
        self.tree = BinaryTree()
        self.tree.insert(self.node1)
        self.tree.insert(self.node2)
        self.tree.insert(self.node3)
        self.tree.insert(self.node4)
        self.tree.insert(self.node5)
        self.tree.insert(self.node6)
        self.tree.insert(self.node7)

    
    def test_find_smallest_2(self):
        self.assertEqual(self.tree.find_smallest(), 1)

class TestSmallestNode3(unittest.TestCase):
    
    def setUp(self):
        self.node1 = Node(1)
        self.node2 = Node(2)
        self.node3 = Node(4)
        self.node4 = Node(5)
        self.node5 = Node(18)
        self.node6 = Node(7)
        self.node7 = Node(12)
        self.tree = BinaryTree()
        self.tree.insert(self.node1)
        self.tree.insert(self.node2)
        self.tree.insert(self.node3)
        self.tree.insert(self.node4)
        self.tree.insert(self.node5)
        self.tree.insert(self.node6)
        self.tree.insert(self.node7)

    
    def test_find_smallest_3(self):
        self.assertEqual(self.tree.find_smallest(), 1)


if __name__ == "__main__":
    unittest.main()