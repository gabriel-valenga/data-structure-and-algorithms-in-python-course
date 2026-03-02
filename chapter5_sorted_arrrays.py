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
