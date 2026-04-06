import numpy as np
from chapter6_stack import Stack
from chapter7_linked_lists import LinkedList


class LinkedListStack(Stack):

    def __init__(self, size):
        super().__init__(size=size, type=LinkedList)


    def stack_is_empty(self):
        return super().stack_is_empty()


    def push_value(self, linked_list=LinkedList):
        return super().push_value(value=linked_list)


    def pop_value_from_the_top(self):
        return super().pop_value_from_the_top()


    def top(self):
        return super().top()


test_list_one = LinkedList()
test_list_one.insert_at_start(1)
test_list_one.insert_at_start(2)

test_list_two = LinkedList()
test_list_two.insert_at_start(3)
test_list_two.insert_at_start(4)

test_list_three = LinkedList()
test_list_three.insert_at_start(5)
test_list_three.insert_at_start(6)

test_stack = LinkedListStack(size=3)
print(f'Stack is empty? {test_stack.stack_is_empty()}')
print(f'Stack is full? {test_stack.stack_is_full()}')
test_stack.push_value(test_list_one)
print(test_stack.top())
test_stack.push_value(test_list_two)
print(test_stack.top())
test_stack.push_value(test_list_three)
print(test_stack.top())
print(f'Stack is full? {test_stack.stack_is_full()}')
test_stack.pop_value_from_the_top()
print(test_stack.top())


print('test')