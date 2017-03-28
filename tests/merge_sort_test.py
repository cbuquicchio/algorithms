from unittest import TestCase
from algorithms import merge_sort


class TestMergeSort(TestCase):
    def test_merge(self):
        A = [1, 3, 5]
        B = [2, 4, 6]
        res = merge_sort.merge(A, B)

        self.assertEqual(res, [1, 2, 3, 4, 5, 6])

    def test_sort(self):
        A = [5, 2, 4, 6, 1, 3]
        res = merge_sort.sort(A)

        self.assertEqual(res, [1, 2, 3, 4, 5, 6])
