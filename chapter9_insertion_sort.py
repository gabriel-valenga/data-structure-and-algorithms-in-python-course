#Insertion sort: number of changes = N*(N-1)/2, number of comparisons = N*(N-1)/4
import numpy as np


def insertion_sort(array):
    n = len(array)
    for i in range(1, n):
        marked = array[i]
        j = i - 1
        while j >= 0 and marked < array[j]:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = marked
    return array

test_array = np.array([5, 70, 42, 2, 10])
test_sorted_array = insertion_sort(test_array)
