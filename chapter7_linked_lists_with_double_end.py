class Node():

    def __init__(self, value):
        self.value = value
        self.next = None


    def show_node(self):
        print(self.value)


class LinkedListWithDoubleEnd():
    
    def __init__(self):
        self.first = None
        self.last = None 


    def list_is_empty(self):
        return self.first == None


    def insert_at_start(self, value):
        new = Node(value=value)
        if self.list_is_empty():
            self.last = new
        new.next = self.first
        self.first = new 


    def insert_at_end(self, value):
        new = Node(value=value)
        if self.list_is_empty():
            self.first = new
        else:
            self.last.next = new
        self.last = new


    def delete_from_start(self):
        if self.list_is_empty():
            return
        temp = self.first
        if self.first.next == None:
            self.last = None
        self.first = self.first.next
        return temp


    def show(self):
        if self.list_is_empty():
            print('List is empty!')
            return 
        current = self.first
        while current != None:
            current.show_node()
            current = current.next


def examples():
    test_list = LinkedListWithDoubleEnd()
    test_list.insert_at_start(1)
    print(test_list.first)
    print(test_list.last)
    test_list.insert_at_end(6)
    test_list.insert_at_start(2)
    test_list.insert_at_start(3)
    test_list.insert_at_end(7)
    test_list.insert_at_start(4)
    test_list.insert_at_start(5)
    test_list.insert_at_end(8)
    test_list.delete_from_start()
    test_list.show()
    print(test_list.first)
    print(test_list.last)
