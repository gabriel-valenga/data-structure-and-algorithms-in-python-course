from chapter7_linked_lists_with_double_end import LinkedListWithDoubleEnd


class LinkedListWithDoubleEndQueue(LinkedListWithDoubleEnd):

    def __init__(self):
        super().__init__()


    def enqueue(self, value):
        return super().insert_at_end(value=value)
    

    def dequeue(self):
        return super().delete_from_start()


    def queue_is_empty(self):
        return super().list_is_empty()
    

    def first(self):
        return super().first


test_linked_list_queue = LinkedListWithDoubleEndQueue()
print(f'queue is empty: {test_linked_list_queue.queue_is_empty()}')
test_linked_list_queue.enqueue(1)
print(f'queue is empty: {test_linked_list_queue.queue_is_empty()}')
test_linked_list_queue.enqueue(2)
print(f'first: {test_linked_list_queue.first.value}')
test_linked_list_queue.enqueue(3)
test_linked_list_queue.show()
print()
test_linked_list_queue.dequeue()
test_linked_list_queue.show()
