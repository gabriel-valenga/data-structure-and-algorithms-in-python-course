def recursion_first_example(execution_times:int=0):
    print('Recursion')
    execution_times += 1
    if execution_times == 5:
        return
    else:
        recursion_first_example(execution_times)

# recursion_first_example()

def sum_example(number:int):
    if number == 0:
        return 0
    return number + sum_example(number - 1)

# print(sum_example(5))

def factorial_example(number:int):
    if number == 0:
        return 1
    return number * factorial_example(number - 1)

#print(factorial_example(3))

def exponentiation_example(base:int, exponent:int):
    if exponent == 0:
        return 1
    return base * exponentiation_example(base, exponent - 1)

print(exponentiation_example(2,4))



