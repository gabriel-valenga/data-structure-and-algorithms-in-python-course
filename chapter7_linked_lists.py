class Node():

    def __init__(self, value):
        self.value = value
        self.next = None


    def show_node(self):
        print(self.value)


class LinkedList():
    
    def __init__(self):
        self.first = None


    def insert_at_start(self, value):
        new = Node(value)
        new.next = self.first
        self.first = new 


    def show(self):
        if self.list_is_empty():
            return
        current = self.first
        while current != None:
            current.show_node()
            current = current.next


    def search(self, value_to_search):
        if self.list_is_empty():
            return
        current = self.first
        while current.value != value_to_search:
            if current.next == None: #end of list
                return None
            else:
                current = current.next
        return current


    def delete_from_start(self):
        if self.list_is_empty():
            return
        temp = self.first    
        self.first = self.first.next
        return temp
    

    def delete_value_from_list(self, value):
        if self.list_is_empty():
            return
        current = self.first 
        previous = self.first
        while current.value != value:
            if current.next == None:
                return None
            else:
                previous = current
                current = current.next
        if current == self.first:
            current = self.delete_from_start()
        else:
            previous.next = current.next
        return current
    

    def list_is_empty(self):
        if self.first == None:
            print('List is empty')
            return True
        return False


def example():
    test_list = LinkedList()
    test_list.show()
    test_list.insert_at_start(1)
    print(test_list.first)
    test_list.show()
    print()
    test_list.insert_at_start(2)
    print(test_list.first)
    test_list.show()
    print()
    test_list.insert_at_start(3)
    print(test_list.first)
    test_list.insert_at_start(4)
    print(test_list.first)
    test_list.insert_at_start(4)
    print(test_list.first)
    test_list.show()
    print(test_list.search(3).value)
    print(test_list.first.next.next.next.next.next)
    print(test_list.first.next.next.next.next)
    print(test_list.first.next.next.next)
    print(test_list.first.next.next)
    print(test_list.first.next)
    print(test_list.first)
    test_list.delete_value_from_list(4)
    test_list.show()
    print()
    test_list.delete_value_from_list(3)
    test_list.show()
    print()
    test_list.delete_from_start()
    test_list.show()
    print()
    test_list.delete_from_start()
    test_list.show()
    print()
    test_list.delete_from_start()
    test_list.show()
    print()
    test_list.delete_from_start()
    test_list.show()
    search = test_list.search(3)
    print(search.value if search is not None else '3 Not Found')

