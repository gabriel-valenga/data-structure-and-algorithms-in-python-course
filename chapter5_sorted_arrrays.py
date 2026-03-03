import numpy as np

class SortedArray:

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


    #O(n)
    def insert(self, value):
        if self.last_position == self.size - 1: #O(1)
            print("Array is full")
        else:
            position = 0
            for i in range(self.last_position + 1): #O(n)
                position = i
                if self.values[i] > value:
                    break
                if i == self.last_position:
                    position = i + 1    
            x = self.last_position
            while x >= position:    
                self.values[x + 1] = self.values[x]
                x -= 1
            self.values[position] = value
            self.last_position += 1


    #O(n)
    def linear_search(self, value):
        for i in range(self.last_position + 1):
            if self.values[i] > value:
                return -1
            if self.values[i] == value:
                return i
            if i == self.last_position:
                return -1
            

    #O(log n)
    def binary_search(self, value):
        left = 0
        right = self.last_position
        while left <= right:
            middle = (left + right) // 2
            if self.values[middle] == value:
                return middle
            elif self.values[middle] < value:
                left = middle + 1
            else:
                right = middle - 1
        return -1

    #O(n)
    def delete(self, value):
        position = self.linear_search(value)
        if position == -1:
            print("Value not found")
        else:
            for i in range(position, self.last_position):
                self.values[i] = self.values[i + 1]
            self.last_position -= 1


test_array = SortedArray(10)
test_array.print_values()
test_array.insert(6)
test_array.print_values()
test_array.insert(4)
test_array.print_values()
test_array.insert(3)
test_array.print_values()   
test_array.insert(5)
test_array.print_values()   
test_array.insert(1)
test_array.print_values() 
test_array.insert(8)
test_array.print_values()   
print(test_array.linear_search(8))
print(test_array.linear_search(2))
print(test_array.linear_search(3))
print(test_array.linear_search(9))

print(test_array.binary_search(8))
print(test_array.binary_search(2))
print(test_array.binary_search(3))
print(test_array.binary_search(9))
print('deleting 5')
test_array.delete(5)
test_array.print_values()
print('deleting 1')
test_array.delete(1)
test_array.print_values()
print('deleting 8') 
test_array.delete(8)
test_array.print_values()