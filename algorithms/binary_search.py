def search_recur(a, v, i, j):
    if j < i:
        return -1 # Not found

    mid = (i + j) / 2

    if a[mid] > v:
        return search_recur(a, v, i, mid - 1)
    elif a[mid] < v:
        return search_recur(a, v, mid + 1, j)

    return mid

def search(a, v):
    return search_recur(a, v, 0, len(a) - 1)
