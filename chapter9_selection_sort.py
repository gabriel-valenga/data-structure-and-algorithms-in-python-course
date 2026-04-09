import numpy as np

#Selection sort: number of changes = N, number of comparisons = N²/2
def selection_sort(array:list):
    n = len(array)
    for i in range(n):
        lower_id = i
        for j in range(i + 1, n):
            if array[lower_id] > array[j]:
                lower_id = j
        temp = array[i]
        array[i] = array[lower_id]
        array[lower_id] = temp
    return array

test_array = np.array([5, 70, 42, 2, 10])
test_sorted_array = selection_sort(test_array)
print('test')    
