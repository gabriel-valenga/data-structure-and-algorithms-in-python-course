import numpy as np

#Bubble sort: number of changes = N², number of comparisons = N²/2
def bubble_sort(array:np.array):
    n = len(array)
    for i in range(n):
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp
    return array

test_array = np.array([5, 70, 42, 2, 10])
test_sorted_array = bubble_sort(test_array)
