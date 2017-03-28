from unittest import TestCase
from algorithms import heap_sort


class TestHeapSort(TestCase):
    def test_max_heapify(self):
        A = [1, 2, 4]

        heap_sort.max_heapify(A , 0, len(A))

        self.assertEqual(A, [4, 2, 1])

    def test_build_max_heap(self):
        A = [5, 2, 4, 6, 1, 3]

        heap_sort.build_max_heap(A)

        self.assertEqual(A, [6, 5, 4, 2, 1, 3])

    def test_sort(self):
        A = [5, 2, 4, 6, 1, 3]

        heap_sort.sort(A)

        self.assertEqual(A, [1, 2, 3, 4, 5, 6])
