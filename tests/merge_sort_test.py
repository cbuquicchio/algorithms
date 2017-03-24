from unittest import TestCase
from algorithms import merge_sort

A = [5, 2, 4, 6, 1, 3]

class TestMergeSort(TestCase):
    def test_sorted_order(self):
        res = merge_sort.sort(A)
        self.assertEqual(res, [1, 2, 3, 4, 5, 6])
