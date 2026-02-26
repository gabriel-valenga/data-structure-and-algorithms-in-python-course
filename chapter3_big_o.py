from math import log
import numpy as np
import matplotlib.pyplot as plt
import timeit

class General:

    @staticmethod
    def functions_comparison(func1, func2, *args, number=1_000_000):
        print(f"{func1.__name__} result: {func1(*args)}")
        print(f"{func2.__name__} result: {func2(*args)}")

        time1 = timeit.timeit(lambda: func1(*args), number=number)
        time2 = timeit.timeit(lambda: func2(*args), number=number)

        print(f"Time taken by {func1.__name__}: {time1:.6f} seconds")
        print(f"Time taken by {func2.__name__}: {time2:.6f} seconds")

        if time2 < time1:
            speedup = time1 / time2
            print(f"{func2.__name__} is {speedup:.2f}x faster than {func1.__name__}")
        elif time1 < time2:
            speedup = time2 / time1
            print(f"{func1.__name__} is {speedup:.2f}x faster than {func2.__name__}")
        else:
            print("Both functions have the same execution time")

class SumFunctions:

    # n+1 steps to big O notation
    # O(n) because the number of steps grows linearly with n
    # Example: if n = 10, the function will execute 11 steps (0 to 10)
    @staticmethod
    def sum1(n):
        sum = 0
        for i in range(n+1):
            sum += i
        return sum


    # 3 steps to big O notation
    # O(3) the number of steps is constant and does not grow with n
    # Example: if n = 10, the function will execute 3 steps (1 multiplication, 1 addition, 1 division: (10 * 11) / 2)
    @staticmethod
    def sum2(n):
        return (n * (n + 1)) / 2


class ListFunctions:

    # O(n) because the number of steps grows linearly with n
    # Example: if n = 10, the function will execute 10 steps (0 to 9)
    @staticmethod
    def list1(n):
        list = []
        for i in range(n):
            list += [i]
        return list
    
    # O(1) because the number of steps is constant and does not grow with n
    # Example: if n = 10, the function will execute 1 step (creating a range object with 10 elements)
    @staticmethod
    def list2(n):
        return range(n)

def linspace_test():
    n = np.linspace(1, 10, 100)     
    print('test')   

# General().functions_comparison(SumFunctions.sum1, SumFunctions.sum2, 10)
# General().functions_comparison(ListFunctions.list1, ListFunctions.list2, 10)
linspace_test()