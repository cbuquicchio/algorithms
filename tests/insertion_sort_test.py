from unittest import TestCase
from algorithms import insertion_sort


class TestInsertionSort(TestCase):
    def test_sorted(self):
        A = [5, 2, 4, 6, 1, 3]

        insertion_sort.sort(A)

        self.assertEqual(A, [1, 2, 3, 4, 5, 6])
