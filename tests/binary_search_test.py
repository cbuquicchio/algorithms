from unittest import TestCase
from algorithms import binary_search

A = [1, 2, 3, 4, 5]

class TestBinarySearch(TestCase):
    def test_search_result(self):
        res = binary_search.search(A, 2)
        self.assertEqual(res, A.index(2))
