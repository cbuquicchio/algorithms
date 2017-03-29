from unittest import TestCase
from algorithms import binary_search_tree as tree

def create_tree(A):
    T = tree.Tree()

    for el in A:
        N = tree.TreeNode(el)
        T.insert(N)

    return T

class TestTree(TestCase):
    def test_insert(self):
        A = [5, 2, 4, 6, 1, 3]
        T = create_tree(A)

        root = T.root
        self.assertEqual(root.key, 5)
        self.assertEqual(root.leftChild.key, 2)
        self.assertEqual(root.rightChild.key, 6)
        self.assertEqual(root.leftChild.leftChild.key, 1)
        self.assertEqual(root.leftChild.rightChild.key, 4)
        self.assertEqual(root.leftChild.rightChild.leftChild.key, 3)

    def test_delete(self):
        T = create_tree([5, 2])
        T.delete(T.root)
        self.assertEqual(T.root.key, 2)

        T = create_tree([5, 6])
        T.delete(T.root)
        self.assertEqual(T.root.key, 6)

        A = [5, 2, 4, 6, 1, 3]
        T = create_tree(A)
        T.delete(T.root.leftChild)
        self.assertEqual(T.root.leftChild.key, 3)
        self.assertEqual(T.root.leftChild.leftChild.key, 1)
        self.assertEqual(T.root.leftChild.rightChild.key, 4)

    def test_search(self):
        A = [5, 2, 4, 6, 1, 3]
        T = create_tree(A)

        res = T.search(6)
        self.assertEqual(res.key, 6)

        res = T.search(100)
        self.assertEqual(res, None)

    def test_minimum(self):
        A = [5, 2, 4, 6, 1, 3]
        T = create_tree(A)

        res = T.minimum()
        self.assertEqual(res.key, 1)

    def test_maximum(self):
        A = [5, 2, 4, 6, 1, 3]
        T = create_tree(A)

        res = T.maximum()
        self.assertEqual(res.key, 6)

    def test_successor_predecessor(self):
        A = [5, 2, 4, 6, 1, 3]
        T = create_tree(A)

        res = T.successor(T.root.leftChild)
        self.assertEqual(res.key, 3)

        res = T.predecessor(res)
        self.assertEqual(res.key, 2)
