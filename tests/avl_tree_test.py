from unittest import TestCase
from algorithms.avl_tree import AVLTree, TreeNode

def create_tree(A):
    T = AVLTree()

    for el in A:
        N = TreeNode(el)
        T.insert(N)

    return T

class TestAVLTree(TestCase):
    def test_insert_left_heavy(self):
        A = [10, 7, 1]
        T = create_tree(A)
        self.assertEqual(T.root.key, 7)
        self.assertEqual(T.root.height, 1)

        A = [10, 1, 7]
        T = create_tree(A)
        self.assertEqual(T.root.key, 7)
        self.assertEqual(T.root.height, 1)

    def test_insert_right_heavy(self):
        A = [1, 7, 10]
        T = create_tree(A)
        self.assertEqual(T.root.key, 7)
        self.assertEqual(T.root.height, 1)

        A = [10, 7, 1]
        T = create_tree(A)
        self.assertEqual(T.root.key, 7)
        self.assertEqual(T.root.height, 1)
