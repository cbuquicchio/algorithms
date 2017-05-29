from unittest import TestCase
from algorithms.karatsuba import k_multiply

bigNum1 = 3141592653589793238462643383279502884197169399375105820974944592
bigNum2 = 2718281828459045235360287471352662497757247093699959574966967627

class TestKaratsuba(TestCase):
    def test_base_case(self):
        res = k_multiply(2, 1)
        self.assertEqual(res, 2 * 1)

        res = k_multiply(2, 100)
        self.assertEqual(res, 2 * 100)

        res = k_multiply(20, 1)
        self.assertEqual(res, 20 * 1)

    def test_recursion(self):
        res = k_multiply(123, 456)
        self.assertEqual(res, 123 * 456)

        res = k_multiply(1234, 567)
        self.assertEqual(res, 1234 * 567)

        res = k_multiply(12, 5678)
        self.assertEqual(res, 12 * 5678)

        res = k_multiply(5678, 12)
        self.assertEqual(res, 12 * 5678)

        res = k_multiply(bigNum1, bigNum2)
        self.assertEqual(res, bigNum1 * bigNum2)

