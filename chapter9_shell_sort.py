#Standard Shell Sort: approximate number of changes = N², approximate number of comparisons = N²
import numpy as np


def standard_shell_sort(array):
    interval = len(array) // 2
    while interval > 0:
        for i in range(interval, len(array)):
            temp = array[i]
            j = i
            while j >= interval and array[j - interval] > temp:
                array[j] = array[j - interval]
                j -= interval 
            array[j] = temp
        interval //= 2
    return array

# Shell Sort (Hibbard - 1, 3, 7, 15, ..., 2^k - 1):
# comparisons ≈ N^(3/2)
# swaps ≈ N^(3/2)

# Shell Sort (Knuth - (3^k - 1) / 2):
# comparisons ≈ N^(3/2)
# swaps ≈ N^(3/2)

# Shell Sort (Sedgewick 1982):
# comparisons ≈ N^(4/3)
# swaps ≈ N^(4/3)

# Shell Sort (Sedgewick 1986):
# comparisons ≈ N^(4/3)
# swaps ≈ N^(4/3)

# Shell Sort (Pratt - 2^p * 3^q):
# comparisons ≈ N log² N
# swaps ≈ N log² N

# Shell Sort (Tokuda):
# comparisons ≈ N^(4/3) (empirical)
# swaps ≈ N^(4/3)

# Shell Sort (Ciura):
# comparisons ≈ ~ N^(4/3) (empirical, very efficient in practice)
# swaps ≈ ~ N^(4/3)

# Shell Sort (Gonnet & Baeza-Yates):
# comparisons ≈ N^(3/2)
# swaps ≈ N^(3/2)

# Shell Sort (Papernov & Stasevich):
# comparisons ≈ N^(3/2)
# swaps ≈ N^(3/2)


test_array = np.array([5, 70, 42, 2, 10])
test_sorted_array = standard_shell_sort(test_array)