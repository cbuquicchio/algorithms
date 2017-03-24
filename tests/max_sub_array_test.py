from unittest import TestCase
from algorithms import max_sub_array

A = [1, -2, 3, 4, 5]

class TestMaxSubArray(TestCase):
    def test_max_sub_array_find(self):
        self.assertEqual(max_sub_array.find(A), (2, 4, 12))
