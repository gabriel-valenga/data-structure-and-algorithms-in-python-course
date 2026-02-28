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
    labels = ['Constant', 'Logarithmic', 'Linear', 'Log Linear', 'Quadratic', 'Cubic', 'Exponential']
    big_o = [np.ones(n.shape), np.log(n), n, n * np.log(n), n**2, n**3, 2**n]
    plt.figure(figsize=(10, 8))
    plt.ylim(0, 100)
    for i in range(len(big_o)):
        plt.plot(n, big_o[i], label=labels[i])
    plt.legend()
    plt.ylabel('Run time')
    plt.xlabel('Input size (n)')
    plt.show()
    print('test')

list_example = [1, 2, 3, 4, 5]

def constant_function(n): # O(1) because the number of steps is constant and does not grow with n
    print(n[0])
    

def linear_function(n): # O(n) because the number of steps grows linearly with n
    for i in range(n):
        print(i)


def quadratic_function(n): # O(n^2) because the number of steps grows quadratically with n
    for i in range(n):
        for j in range(n):
            print(i, j)


def test_combination(n): # O(1) + O(5) + O(n) + O(1) + O(1) + O(1) = O(n) because n is the dominant term because n its an infinite variable and the other terms are constants
    # O(1)
    print(n[0])

    # O(5)
    for i in range(5):
        print('test', i)

    # O(n)
    for i in n:
        print(i)

    # O(1)
    print('Python')
    # O(1)
    print('Python')
    # O(1)
    print('Python')

# General().functions_comparison(SumFunctions.sum1, SumFunctions.sum2, 10)
# General().functions_comparison(ListFunctions.list1, ListFunctions.list2, 10)
# linspace_test()
test_combination(list_example)    