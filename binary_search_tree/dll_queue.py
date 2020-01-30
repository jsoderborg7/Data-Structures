# import sys
# sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # DLL lets us find the head and tail easily, and the FIFO approach is simple to understand
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        # To queue up, we add the item to the last item of the linked list, and increase its link by 1
        self.storage.add_to_tail(value)
        self.size += 1

    def dequeue(self):
        # first we have to make sure the queue isn't empty
        if self.size > 0:
        # Then we reduce the size and take out the item from the head, and return the value stored in that item
            self.size -= 1
            return self.storage.remove_from_head()

    def len(self):
        return self.size
