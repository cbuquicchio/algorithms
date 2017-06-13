from unittest import TestCase
from algorithms.depth_first_search import search

graph = {
        's': ['r', 'w'],
        'r': ['s', 'v'],
        'w': ['s', 't', 'x'],
        'v': ['r'],
        't': ['w', 'u'],
        'x': ['w', 'u'],
        'u': ['t', 'y'],
        'y': ['u']
        }

class TestDFS(TestCase):
    def test_search(self):
        res = search(graph, 's')
        expected = ['s', 'r', 'v', 'w', 't', 'u', 'y', 'x']

        self.assertEqual(res, expected)
