def find_max_crossing_subarray(A, low, mid, high):
    left_sum = -float('inf')
    right_sum = -float('inf')
    sum = 0
    max_left = None
    max_right = None

    for i in range(mid, low - 1, -1):
        sum += A[i]
        
        if sum > left_sum:
            left_sum = sum
            max_left = i
    
    sum = 0

    for j in range(mid + 1, high+1):
        sum += A[j]

        if sum > right_sum:
            right_sum = sum
            max_right = j

    return (max_left, max_right, left_sum + right_sum)

def max_sub_array_recur(A, low, high):
    if low == high:
        return (low, high, A[low])
    else:
        mid = (low + high) / 2
        (left_low, left_high, left_sum) = max_sub_array_recur(A, low, mid)
        (right_low, right_high, right_sum) = max_sub_array_recur(
                A, mid + 1, high)
        (cross_low, cross_high, cross_sum) = find_max_crossing_subarray(
                A, low, mid, high)

        if left_sum >= right_sum and left_sum >= cross_sum:
            return (left_low, left_high, left_sum)
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return (right_low, right_high, right_sum)
        else:
            return (cross_low, cross_high, cross_sum)

def find(A):
    return max_sub_array_recur(A, 0, len(A) - 1)

### Brute Force Method ###

"""
def max_sub_array(A):
    max_sum = -float('inf')
    left = 0
    right = 0

    for i in range(len(A)):
        sum = 0

        for j in range(i, len(A)):
            sum += A[j]

            if sum > max_sum:
                max_sum = sum
                left = i
                right = j

    return (left, right, max_sum)
"""
