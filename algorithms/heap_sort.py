from utils import swap

def max_heapify(A, i, heap_size):
    l = (i << 1) + 1
    r = l + 1
    largest = i

    if l < heap_size and A[l] > A[i]:
        largest = l

    if r < heap_size and A[r] > A[largest]:
        largest = r

    if largest != i:
        swap(A, i, largest)

        max_heapify(A, largest, heap_size)

def build_max_heap(A):
    for i in range(len(A) - 1, -1, -1):
        max_heapify(A, i, len(A))

def sort(A):
    heap_size = len(A)

    build_max_heap(A)

    for i in range(len(A) - 1, 0, -1):
        swap(A, 0, i)
        heap_size -= 1

        max_heapify(A, 0, heap_size)
