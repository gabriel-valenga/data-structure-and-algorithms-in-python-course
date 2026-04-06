import numpy as np

class PriorityQueue:

    def __init__(self, capacity):
        self.capacity = capacity
        self.number_of_elements = 0
        self.values = np.empty(self.capacity, dtype=int)


    def queue_is_empty(self):
        return self.number_of_elements == 0
    

    def queue_is_full(self):
        return self.number_of_elements == self.capacity
    

    def enqueue(self, value):
        if self.queue_is_full():
            print('The queue is full!')
            return 

        if self.number_of_elements == 0:
            self.values[self.number_of_elements] = value
            self.number_of_elements += 1
        else:
            x = self.number_of_elements - 1
            while x >= 0:
                if value > self.values[x]:
                    self.values[x + 1] = self.values[x]
                else:
                    break 
                x -=1
            self.values[x+1] = value
            self.number_of_elements += 1


    def dequeue(self):
        if self.queue_is_empty():
            print('The queue is empty!')
            return 
        value = self.values[self.number_of_elements-1]
        self.number_of_elements -= 1
        return value


    def first(self):
        if self.queue_is_empty():
            return -1 
        return self.values[self.number_of_elements - 1]
    

    def return_queue_in_format_of_a_list(self):
        return self.values.tolist()
    

def examples():
    queue = PriorityQueue(5)
    print(queue.first())
    queue.enqueue(30)
    print(queue.return_queue_in_format_of_a_list())
    print(queue.first())
    queue.enqueue(50)
    print(queue.return_queue_in_format_of_a_list())
    print(queue.first())
    queue.enqueue(10)
    print(queue.return_queue_in_format_of_a_list())
    print(queue.first())
    queue.enqueue(40)
    print(queue.return_queue_in_format_of_a_list())
    print(queue.first())
    queue.enqueue(20)
    print(queue.return_queue_in_format_of_a_list())
    print(queue.first())
    queue.enqueue(2)
    queue.dequeue()
    print(queue.return_queue_in_format_of_a_list())
    print(queue.first())
    queue.dequeue()
    print(queue.return_queue_in_format_of_a_list())
    print(queue.first())
    queue.dequeue()
    print(queue.return_queue_in_format_of_a_list())
    print(queue.first())
    queue.enqueue(5)
    print(queue.return_queue_in_format_of_a_list())
    print(queue.first())
