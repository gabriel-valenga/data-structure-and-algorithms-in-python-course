import numpy as np

class UnsortedArray:

    def __init__(self, size):
        self.size = size
        self.last_position = -1
        self.values = np.empty(self.size, dtype=int)

    
    #O(n)    
    def print_values(self):
        if self.last_position == -1:
            print("Array is empty")
        else:
            for i in range(self.last_position + 1):
                print(i, " - ", self.values[i])
            print()

    #O(3)
    def insert(self, value):
        if self.last_position == self.size - 1: #O(1)
            print("Array is full")
        else:
            self.last_position += 1 #O(1)
            self.values[self.last_position] = value #O


    #O(n)
    def search(self, value):
        for i in range(self.last_position + 1):
            if self.values[i] == value:
                return i
        return -1
    
    #O(n)
    def delete(self, value):
        position = self.search(value)
        if position == -1:
            print("Value not found")
        else:
            for i in range(position, self.last_position):
                self.values[i] = self.values[i + 1]
            self.last_position -= 1


test_array = UnsortedArray(5)
test_array.print_values()
test_array.insert(3)
test_array.insert(5)
test_array.insert(8)
test_array.insert(1)
test_array.insert(7)
test_array.print_values()
test_array.insert(10)
print(test_array.last_position)
print(test_array.search(8))
print(test_array.search(9))
print(test_array.search(3))
test_array.print_values()
print('deleting 5')
test_array.delete(5)
test_array.print_values()
print('deleting 3')
test_array.delete(3)
test_array.print_values()
print('deleting 10')
test_array.delete(10)
test_array.print_values()
print('deleting 7')
test_array.delete(7)
test_array.print_values()