def merge(left, right):
    i = 0
    j = 0
    result = []

    while i < len(left) or j < len(right):
        if i >= len(left):
            result.append(right[j])
            j += 1
        elif j >= len(right):
            result.append(left[i])
            i += 1
        elif left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    return result

def merge_sort_recur(A):
    if len(A) < 2:
        return A

    mid = len(A) / 2

    left = merge_sort_recur(A[:mid])
    right = merge_sort_recur(A[mid:])
    
    return merge(left, right)

def merge_sort(A):
    return merge_sort_recur(A)
