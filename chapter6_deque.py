import numpy as np

class Deque:

    def __init__(self, capacity):
        self.capacity = capacity
        self.start = 0
        self.end = -1
        self.number_of_elements = 0
        self.values = np.empty(self.capacity, dtype=int)


    def __deque_is_full(self):
        return (self.start == 0 and self.end == self.capacity - 1) or (self.start == self.end + 1)
    

    def __deque_is_empty(self):
        return self.start == -1
    

    def insert_value_at_start(self, value:int):
        if self.__deque_is_full():
            print('Deque is full!')
            return
        if self.__deque_is_empty():
            self.start = 0
            self.end = 0
        #if starts at first position
        elif self.start == 0:
            self.start = self.capacity - 1
        else:
            self.start -= 1

        self.values[self.start] = value
    

    def insert_value_at_end(self, value:int):
        if self.__deque_is_full():
            print('Deque is full!')
            return
        if self.__deque_is_empty():
            self.start = 0
            self.end = 0
        # if ends at last position
        elif self.end == self.capacity - 1:
            self.end = 0
        else:
            self.end += 1
        self.values[self.end] = value


    def delete_from_start(self):
        if self.__deque_is_empty():
            print('Deque is empty!')
            return 
        #if has only one element
        if self.start == self.end:
            self.start = -1
            self.end = -1
        elif self.start == self.capacity - 1: #back to start position
            self.start = 0
        else:
            #increase start position to remove current start position
            self.start += 1
            


    def delete_from_end(self):
        if self.__deque_is_empty():
            print('Deque is empty!')
            return 
        #if has only one element
        if self.start == self.end:
            self.start = -1
            self.end = -1
        elif self.start == 0: #back to end position
            self.end = self.capacity - 1
        else:
            #increase end position to remove current end position
            self.end -= 1    
