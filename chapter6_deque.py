import numpy as np

class Deque:

    def __init__(self, capacity):
        self.capacity = capacity
        self.start_position = -1
        self.end_position = 0
        self.number_of_elements = 0
        self.values = np.empty(self.capacity, dtype=int)


    def __deque_is_full(self):
        return self.number_of_elements == self.capacity
    

    def __deque_is_empty(self):
        return self.number_of_elements == 0
    

    def insert_value_at_start_position(self, value:int):
        if self.__deque_is_full():
            print('Deque is full!')
            return
        if self.__deque_is_empty():
            self.start_position = 0
            self.end_position = 0
        else:
        #if start_position is at first position
            if self.start_position == 0:
                self.start_position = self.capacity -1
            else:
                self.start_position -= 1
        self.number_of_elements += 1
        self.values[self.start_position] = value
    

    def insert_value_at_end_position(self, value:int):
        if self.__deque_is_full():
            print('Deque is full!')
            return
        if self.__deque_is_empty():
            self.start_position = 0
            self.end_position = 0
        else:
            # if end_position is at last position
            if self.end_position == self.capacity - 1:
                self.end_position = 0
            else:
                self.end_position += 1
        self.number_of_elements += 1
        self.values[self.end_position] = value


    def delete_from_start_position(self):
        if self.__deque_is_empty():
            print('Deque is empty!')
            return 
        #if has only one element
        if self.start_position == self.end_position:
            self.start_position = -1
            self.end_position = -1
        elif self.start_position == self.capacity - 1: #back to start_position position
            self.start_position = 0
        else:
            #increase start_position position to remove current start_position position
            self.start_position += 1
            

    def delete_from_end_position(self):
        if self.__deque_is_empty():
            print('Deque is empty!')
            return 
        #if has only one element
        if self.start_position == self.end_position:
            self.start_position = -1
            self.end_position = -1
        elif self.start_position == 0: #back to end_position position
            self.end_position = self.capacity - 1
        else:
            #increase end_position position to remove current end_position position
            self.end_position -= 1    


    def get_start_value(self):
        if self.__deque_is_empty():
            print('Deque is empty!')
            return 
        return self.values[self.start_position]
    

    def get_end_value(self):
        if self.__deque_is_empty():
            print('Deque is empty!')
            return 
        return self.values[self.end_position]
    
deque = Deque(5)
deque.insert_value_at_end_position(5)
print(deque.get_start_value())
print(deque.get_end_value())
print(deque.values)
deque.insert_value_at_end_position(10)
print(deque.get_start_value())
print(deque.get_end_value())
print(deque.values)
deque.insert_value_at_start_position(3)
print(deque.get_start_value())
print(deque.get_end_value())
print(deque.values)
deque.insert_value_at_start_position(2)
deque.insert_value_at_end_position(11)
print(deque.get_start_value())
print(deque.get_end_value())
print(deque.values)
deque.delete_from_start_position()
deque.delete_from_end_position()
print(deque.get_start_value())
print(deque.get_end_value())
print(deque.values)
