class Node():

    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None


    def show_node(self):
        print(self.value)


class DoublyLinkedList:

    def __init__(self):
        self.first = None
        self.last = None


    def __empty_list(self):
        return self.first == None
    

    def insert_at_start(self, value):
        new = Node(value)
        if self.__empty_list():
            self.last = new
        else:
            self.first.previous = new
        new.next = self.first
        self.first = new


    def insert_at_end(self, value):
        new = Node(value)
        if self.__empty_list():
            self.first = new 
        else:
            self.last.next = new
            new.previous = self.last
            self.last = new


    def show_values_from_start_to_end(self):
        current = self.first
        while current != None:
            current.show_node()
            current = current.next


    def show_values_from_end_to_start(self):
        current = self.last
        while current != None:
            current.show_node()
            current = current.previous


test_list = DoublyLinkedList()
test_list.insert_at_start(1)
test_list.insert_at_start(2)
test_list.insert_at_end(3)
test_list.insert_at_end(4)
print()
test_list.show_values_from_start_to_end()
print()
test_list.show_values_from_end_to_start()
print()
test_list.insert_at_start(5)
test_list.show_values_from_start_to_end()
print()
test_list.show_values_from_end_to_start()
