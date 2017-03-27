from unittest import TestCase
from algorithms import quick_sort


class TestQuickSort(TestCase):
    def test_partition(self):
        A = [5, 1, 6, 4, 2, 3]
        res = quick_sort.partition(A, 0, len(A) - 1)

        self.assertEqual(A, [1, 2, 3, 4, 5, 6])
        self.assertEqual(res, 2)

    def test_sorted_order(self):
        A = [5, 1, 6, 4, 2, 3]
        quick_sort.sort(A)

        self.assertEqual(A, [1, 2, 3, 4, 5, 6])
