# import sys
# sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # stack is kind of like queue, except we're only working with the head node
        self.storage = DoublyLinkedList()


    def push(self, value):
        # stacks always add to the head
        self.storage.add_to_head(value)
        self.size += 1



    def pop(self):
        # stacks remove from the head
        if self.size > 0:
            self.size -= 1
            return self.storage.remove_from_head()

    def len(self):
        return self.size
