from unittest import TestCase
from algorithms import heap_sort

A = [5, 2, 4, 6, 1, 3]
B = [5, 2, 4, 6, 1, 3]

class TestHeapSort(TestCase):
    def test_max_heapify(self):
        heap = [1, 2, 4]
        heap_sort.max_heapify(heap, 0, len(heap))
        self.assertEqual(heap, [4, 2, 1])

    def test_build_max_heap(self):
        heap_sort.build_max_heap(A)
        self.assertEqual(A, [6, 5, 4, 2, 1, 3])

    def test_heap_sort_order(self):
        heap_sort.sort(B)
        self.assertEqual(B, [1, 2, 3, 4, 5, 6])
