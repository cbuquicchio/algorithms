from unittest import TestCase
from algorithms.breadth_first_search import bfs

def follow_path(paths, src):
    path = []

    while paths[src] != None:
        path.append(paths[src])
        src = paths[src]

    return path

class TestBFS(TestCase):
    def test_bfs(self):
        graph = {}

        graph['s'] = ['r', 'w']
        graph['r'] = ['s', 'v']
        graph['w'] = ['s', 't', 'x']
        graph['v'] = ['r']
        graph['t'] = ['w', 'u']
        graph['x'] = ['w', 'u']
        graph['u'] = ['t', 'y']
        graph['y'] = ['u']

        dists, paths = bfs(graph, 's')
        expected_dists = {
                's': 0, 'r': 1, 'w': 1,
                'v': 2, 't': 2, 'x': 2,
                'u': 3, 'y': 4 }

        path_from_y = follow_path(paths, 'y')
        expected_path_from_y = ['u', 't', 'w', 's']

        self.assertEqual(dists, expected_dists)
        self.assertEqual(path_from_y, expected_path_from_y)
        self.assertEqual(len(path_from_y), expected_dists['y'])
