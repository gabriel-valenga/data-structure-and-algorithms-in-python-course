import numpy as np


class Stack:

    def __init__(self, size):
        self.__size = size
        self.__top = -1
        self.__values = np.empty(size, dtype=int)


    def __stack_is_full(self):
        if self.__top == self.__size - 1:
            return True
        else:
            return False
    

    def __stack_is_empty(self):
        if self.__top == -1:
            return True
        else:
            return False
        

    def push_value(self, value):
        if self.__stack_is_full():
            print("Stack is full. Cannot push value.")
        else:
            self.__top += 1
            self.__values[self.__top] = value


    def pop_value_from_the_top(self):
        if self.__stack_is_empty():
            print("Stack is empty. Cannot pop value.")
        else:
            self.__top -= 1
        

    def top(self):
        if self.__stack_is_empty():
            return -1
        else:
            return self.__values[self.__top]
        

stack = Stack(5)
print(stack.top())
stack.push_value(1)
print(stack.top())
stack.push_value(2)
stack.push_value(3)
stack.push_value(4)
stack.push_value(5)
stack.push_value(6)
print(stack.top())
stack.pop_value_from_the_top()
print(stack.top())
stack.pop_value_from_the_top()
print(stack.top())
stack.pop_value_from_the_top()
print(stack.top())
stack.pop_value_from_the_top()
print(stack.top())
stack.pop_value_from_the_top()
print(stack.top())
stack.pop_value_from_the_top()