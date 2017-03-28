from unittest import TestCase
from algorithms import max_sub_array


class TestMaxSubArray(TestCase):
    def test_find_max_crossing_subarray(self):
        A = [1, -2, 3, 4, 5]
        low = 0
        high = len(A) - 1
        mid = (low + high) / 2
        res = max_sub_array.find_max_crossing_subarray(A, low, mid, high)

        self.assertEqual(res, (2, 4, 12))


    def test_find(self):
        A = [1, -2, 3, 4, 5]
        res = max_sub_array.find(A)

        self.assertEqual(res, (2, 4, 12))
