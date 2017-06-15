from copy import copy
from random import seed
from unittest import TestCase
from algorithms.quick_sort import partition, sort


class TestQuickSort(TestCase):
    def setUp(self):
        self.A = [5, 1, 6, 4, 2, 3]

    def test_partition(self):
        seed(17) # should result in index 3 selected as pivot

        A = self.A
        res = partition(A, 0, len(A) - 1)

        self.assertEqual(A, [3, 1, 2, 4, 6, 5])
        self.assertEqual(res, 3)

    def test_sorted_order(self):
        res = True

        seed(None)

        # run sort multiple time to check randomized pivot implementation
        for i in xrange(100):
            A = copy(self.A)
            sort(A)

            if A != [1, 2, 3, 4, 5, 6]:
                res = False
                break

        self.assertEqual(res, True)
