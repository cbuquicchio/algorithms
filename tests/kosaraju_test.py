from unittest import TestCase
from algorithms.kosaraju import (find_strong_components, graph_reverse,
        find_iterative)

graph = {
        '1': ['4'],
        '2': ['3'],
        '3': ['10'],
        '4': ['3', '5'],
        '5': ['4', '8'],
        '6': ['1', '10'],
        '7': ['2', '3'],
        '8': ['10'],
        '9': ['1', '6'],
        '10': ['2', '7']
        }

class TestKosaraju(TestCase):
    def test_graph_reverse(self):
        res = graph_reverse(graph)
        expected = {
                '1': ['6', '9'],
                '2': ['10', '7'],
                '3': ['2', '4', '7'],
                '4': ['1', '5'],
                '5': ['4'],
                '6': ['9'],
                '7': ['10'],
                '8': ['5'],
                '10': ['3', '6', '8']
                }

        self.assertEqual(res, expected)

    def test_find_scc(self):
        res = find_strong_components(graph)
        expected = {
                '10': ['10', '2', '3', '7'],
                '1': ['1'],
                '4': ['4', '5'],
                '6': ['6'],
                '8': ['8'],
                '9': ['9']
                }

        self.assertEqual(res, expected)

    def test_iterative_scc(self):
        res = find_iterative(graph)
        expected = {
                '10': set(['10', '2', '3', '7']),
                '1': set(['1']),
                '4': set(['4', '5']),
                '6': set(['6']),
                '8': set(['8']),
                '9': set(['9'])
                }

        self.assertEqual(res, expected)
