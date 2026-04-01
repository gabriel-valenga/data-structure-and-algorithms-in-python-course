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


    def delete_from_start(self):
        temp = self.first
        if self.first.next == None:
            self.last = None
        else:
            self.first.next.previous = None
        self.first = self.first.next
        return temp
    

    def delete_from_end(self):
        temp = self.last
        if self.first.next == None:
            self.first = None
        else:
            self.last.previous.next = None
        self.last = self.last.previous
        return temp


    def delete_value_from_list(self, value):
        current = self.first
        while current.value != value:
            current = current.next
            if current == None:
                return None
        if current == self.first:
            self.first = current.next
        else:
            current.previous.next = current.next
        if current == self.last:
            self.last = current.previous
        else:
            current.next.previous = current.previous
        return current
    

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
print(f'last value: {test_list.last.value}')
test_list.delete_from_end()
print(f'last value: {test_list.last.value}')
print()
print(f'first value: {test_list.first.value}')
print()
test_list.delete_from_start()
print(f'first value: {test_list.first.value}')
test_list.show_values_from_end_to_start()
print()
test_list.delete_value_from_list(1)
test_list.show_values_from_start_to_end()
