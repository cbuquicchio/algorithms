from unittest import TestCase
from algorithms import insertion_sort

A = [5, 2, 4, 6, 1, 3]

class TestInsertionSort(TestCase):
    def test_sorted_order(self):
        insertion_sort.sort(A)
        self.assertEqual(A, [1, 2, 3, 4, 5, 6])
