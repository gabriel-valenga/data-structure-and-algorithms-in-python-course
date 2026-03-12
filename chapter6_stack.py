import numpy as np


class Stack:

    def __init__(self, size, type):
        self.__size = size
        self.__type = type
        self.__top = -1
        self.__values = np.empty(size, dtype=type)


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
        expression_delimiter_characters = '{([])}'
        close_delimiters = '}])'
        expression_delimiter_characters_pairs = {
           '}':'{',
           ']':'[',
           ')':'('
        }
        check_expression_delimiters_stack = Stack(len(self.list_of_expression_characters), type=type) 
        current_close_delimiter = None
        for charactere in self.list_of_expression_characters:
            if charactere in expression_delimiter_characters:
                check_expression_delimiters_stack.push_value(charactere)
        check_expression_delimiters_stack_copy = check_expression_delimiters_stack.copy()
        for delimiter in reversed(check_expression_delimiters_stack_copy): #browse the copy stack, remove from original stack
            if delimiter is None:
                continue
            current_open_delimiter = check_expression_delimiters_stack.top() 
            if delimiter in close_delimiters:
                current_close_delimiter = delimiter
            if current_close_delimiter is None:
                continue
            if current_open_delimiter is not None: #here in this block below you have to change the logic trading open_delimiter and close_delimiter
                if current_close_delimiter is None:
                    print('Error in expression: open delimiter without close delimiter')
                    return 
                else:
                    correct_open_delimiter = expression_delimiter_characters_pairs.get(current_close_delimiter)
                    if current_open_delimiter != correct_open_delimiter:
                        print('Error in expression: wrong open delimiter')
                        return
        print('The expression is correct!')    
            



exercise_one = ExerciseOneExpressionMatcher(expression='a{b(c[d]e)f}', type=str)
exercise_one.expression_matcher()
exercise_one = ExerciseOneExpressionMatcher(expression='a{b(cd]e)f}', type=str)
exercise_one.expression_matcher()

    

    