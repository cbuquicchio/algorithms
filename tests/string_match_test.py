from unittest import TestCase
from algorithms.string_match import string_match

class TestStringMatch(TestCase):
    def test_single_match(self):
        pattern = 'hello'
        res = string_match(pattern, 'hello world', 5)

        self.assertEqual(len(res), 1)

        res = string_match(pattern, 'hello', 5)

        self.assertEqual(len(res), 1)

        res = string_match(pattern, ' hello', 5)

        self.assertEqual(len(res), 1)

        res = string_match(pattern, 'world hello', 5)

        self.assertEqual(len(res), 1)

    def test_multi_match(self):
        pattern = 'hello'
        text = 'hello this is hello world helloasdf asdflkja aisdf asdkfjal;sdf asdf aksjdflajs;dflkjas;dlkfj'
        res = string_match(pattern, text, 13)

        self.assertEqual(len(res), 3)
