# Merge Sort: comparisons ≈ N log N | swaps ≈ N log N
import numpy as np


def merge_sort(array:np.array):
    if len(array) <= 1:
        return array
    division = len(array) // 2
    left = array[:division].copy()
    right = array[division:].copy()
    merge_sort(left)
    merge_sort(right)
    i = j = k = 0
    #order left and right
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
        k += 1
    #final order
    while i < len(left):
        array[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        array[k] = right[j]
        j += 1
        k += 1
    return array


test_array = np.array([5, 70, 42, 2, 10])
test_sorted_array = merge_sort(test_array)
print('teste')