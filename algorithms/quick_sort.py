from utils import swap

def partition(A, p, r):
    i = p - 1
    pivot = A[r]

    for j in range(p, r):
        if A[j] <= pivot:
            i += 1
            swap(A, i, j)

    i += 1
    swap(A, i, r)

    return i

def quick_sort(A, p, r):
    if p <= r:
        q = partition(A, p, r)
        quick_sort(A, p, q - 1)
        quick_sort(A, q + 1, r)

def sort(A):
    quick_sort(A, 0, len(A) - 1)
