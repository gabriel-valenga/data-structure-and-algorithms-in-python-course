import numpy as np

# Quick Sort (average case): comparisons ≈ N log N | swaps ≈ N log N
# Quick Sort (worst case): comparisons ≈ N² | swaps ≈ N²

def partition(array, start, end):
    pivot = array[end]
    i = start - 1

    for j in range(start, end):
        if array[j] <= pivot:
            i += 1
            array[i] , array[j] = array[j], array[i]
    array[i+1], array[end] = array[end], array[i + 1]
    return i + 1


def quick_sort(array, start=0, end=None):
    if not end:
        end = len(array) - 1
    if start < end:
        position = partition(array, start, end)
        # order left part
        quick_sort(array, start, position - 1)
        # order right part
        quick_sort(array, position + 1, end)
    return array

test_array = np.array([5, 70, 42, 2, 10])
test_sorted_array = quick_sort(test_array)
