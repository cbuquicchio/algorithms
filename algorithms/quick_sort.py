from random import randint
from utils import swap

def select_pivot(A, lo, hi):
    p = randint(lo, hi)
    swap(A, lo, p)

    return lo


def partition(A, lo, hi):
    p = select_pivot(A, lo, hi)
    i = lo + 1

    for j in xrange(i, hi + 1):
        if A[j] < A[p]:
            swap(A, i, j)
            i += 1

    swap(A, i-1, p)
    return i-1

def quick_sort(A, lo, hi):
    if lo >= hi:
        return

    p = partition(A, lo, hi)
    quick_sort(A, lo, p - 1)
    quick_sort(A, p + 1, hi)

def sort(A):
    quick_sort(A, 0, len(A) - 1)
