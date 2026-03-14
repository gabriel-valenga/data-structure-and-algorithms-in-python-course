import numpy as np

class CircularQueue:

    def __init__(self, capacity):
        self.capacity = capacity
        self.start = 0
        self.end = -1
        self.number_of_elements = 0
        self.values = np.empty(self.capacity, dtype=int)


    def __queue_is_empty(self):
        return self.number_of_elements == 0
    

    def __queue_is_full(self):
        return self.number_of_elements == self.capacity
    

    def line_up(self, value):
        if self.__queue_is_full():
            print('The queue is full')
            return 
        if self.end == self.capacity - 1:
            self.end = -1
        self.end += 1
        self.values[self.end] = value 
        self.number_of_elements += 1

    
    def dequeue(self):
        if self.__queue_is_empty():
            print("Queue it's already empty")
            return 
        temp = self.values[self.start]
        self.start += 1
        if self.start == self.capacity - 1:
            self.start = 0
        self.number_of_elements -= 1
        return temp
    

    def first(self):
        if self.__queue_is_empty():
            return -1 
        return self.values[self.start]
    

    def return_queue_in_format_of_a_list(self):
        return self.values.tolist()
    

queue = CircularQueue(5)
queue.dequeue()
queue.line_up(1)
print(queue.return_queue_in_format_of_a_list())
queue.line_up(2)
print(queue.return_queue_in_format_of_a_list())
print(f'first element of queue: {queue.first()}')
queue.line_up(3)
print(queue.return_queue_in_format_of_a_list())
print(f'first element of queue: {queue.first()}')
queue.line_up(4)
print(queue.return_queue_in_format_of_a_list())
queue.line_up(5)
print(queue.return_queue_in_format_of_a_list())
print(f'first element of queue: {queue.first()}')
queue.line_up(6)
queue.dequeue()
print(queue.return_queue_in_format_of_a_list())
print(f'first element of queue: {queue.first()}')
queue.dequeue()
print(queue.return_queue_in_format_of_a_list())
print(f'first element of queue: {queue.first()}')
queue.line_up(6)
print(queue.return_queue_in_format_of_a_list())
print(f'first element of queue: {queue.first()}')
queue.line_up(7)
print(queue.return_queue_in_format_of_a_list())
print(f'first element of queue: {queue.first()}')



