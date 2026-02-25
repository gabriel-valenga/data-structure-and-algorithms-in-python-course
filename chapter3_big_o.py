import timeit

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



    def sum_functions_comparison(self, n):
        print(f"Sum1 result: {self.sum1(n)}")
        print(f"Sum2 result: {self.sum2(n)}")
        time_sum_1 = timeit.timeit(lambda: self.sum1(n), globals=globals(), number=1000000)
        time_sum_2 = timeit.timeit(lambda: self.sum2(n), globals=globals(), number=1000000)
        print(f"Time taken by sum1: {time_sum_1} seconds")
        print(f"Time taken by sum2: {time_sum_2} seconds")
        if time_sum_2 < time_sum_1:
            speedup = time_sum_1 / time_sum_2
            print(f"sum_2 is {speedup:.2f}x faster than sum_1")
        elif time_sum_1 < time_sum_2:
            speedup = time_sum_2 / time_sum_1
            print(f"sum_1 is {speedup:.2f}x faster than sum_2")
        else:
            print("Both functions have the same execution time")

SumFunctions().sum_functions_comparison(10)
