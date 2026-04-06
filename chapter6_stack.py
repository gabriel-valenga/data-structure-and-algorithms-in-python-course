import numpy as np


class Stack:

    def __init__(self, size, type):
        self.__size = size
        self.__type = type
        self.__top = -1
        self.__values = np.empty(size, dtype=type)


    def stack_is_full(self):
        if self.__top == self.__size - 1:
            return True
        else:
            return False
    

    def stack_is_empty(self):
        if self.__top == -1:
            return True
        else:
            return False
        

    def push_value(self, value):
        if self.stack_is_full():
            print("Stack is full. Cannot push value.")
        else:
            self.__top += 1
            self.__values[self.__top] = value


    def pop_value_from_the_top(self):
        if self.stack_is_empty():
            print("Stack is empty. Cannot pop value.")
        else:
            self.__top -= 1
        

    def top(self):
        if self.stack_is_empty():
            return -1
        else:
            return self.__values[self.__top]
        

    def values(self):
        return self.__values
    

    def copy(self):
        new_stack = Stack(size=self.__size, type=self.__type)
        new_stack.__values = self.__values.copy()
        new_stack.__top = self.__top
        return new_stack
        

def example_one():
    stack = Stack(5, type=int)
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


class ExerciseOneExpressionMatcher:

    def __init__(self, expression, type):
        self.expression = expression
        self.list_of_expression_characters = list(expression)


    def expression_matcher(self):
        open_delimiters = '{(['
        close_delimiters = '}])'
        expression_delimiter_characters_pairs = {
           '}':'{',
           ']':'[',
           ')':'('
        }
        expression_open_delimiters_stack = Stack(size=len(self.expression), type=str)
        for charactere in self.expression:
            if charactere in open_delimiters:
                expression_open_delimiters_stack.push_value(charactere)
            if charactere in close_delimiters:
                correct_open_delimiter = expression_delimiter_characters_pairs.get(charactere)
                if expression_open_delimiters_stack.top() == correct_open_delimiter:
                    expression_open_delimiters_stack.pop_value_from_the_top()
                else:
                    print('Error: invalid expression!')
                    return
        print('Success: valid expression!')


def exercise_one():
    exercise_one = ExerciseOneExpressionMatcher(expression='a{b(c[d]e)f}', type=str)
    exercise_one.expression_matcher()
    exercise_one = ExerciseOneExpressionMatcher(expression='a{b(cd]e)f}', type=str)
    exercise_one.expression_matcher()
    exercise_one = ExerciseOneExpressionMatcher(expression='ab(c[d]e)f}', type=str)
    exercise_one.expression_matcher()


# example_one()          
# exercise_one()
