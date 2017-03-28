from unittest import TestCase
from algorithms import binary_search


class TestBinarySearch(TestCase):
    def test_search(self):
        A = [1, 2, 3, 4, 5]
        res = binary_search.search(A, 2)

        self.assertEqual(res, A.index(2))
