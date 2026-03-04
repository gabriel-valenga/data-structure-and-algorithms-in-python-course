import timeit

def functions_comparison(func1, func2, *args):
    print(f"{func1.__name__} result: {func1(*args)}")
    print(f"{func2.__name__} result: {func2(*args)}")

    time1 = timeit.timeit(lambda: func1(*args), number=1)
    time2 = timeit.timeit(lambda: func2(*args), number=1)

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
