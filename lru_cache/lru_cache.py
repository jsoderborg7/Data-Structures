from doubly_linked_list import DoublyLinkedList

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
    # assign max size of cache with default limit
        self.limit = limit
    # assign cache start size
        self.size = 0
    # order the list
        self.order = DoublyLinkedList()
    # store keys and values
        self.storage = {}

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
    # check the storage for the key
        if key in self.storage:
    # if found, set as node for look up
            node = self.storage[key]
    # use the DLL method move-to-end to move the node from its current position to the end front of the list
            self.order.move_to_end(node)
            return node.value[1]
    # if the key isn't in the cache, return nothing
        else:
            return None

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
    # check storage for key
        if key in self.storage:
    # if it's there, set it as the node
            node = self.storage[key]
    # store the node value as a tuple
            node.value = (key, value)
    # move it to the end
            self.order.move_to_end(node)
            return
    # if it is in the cache, move it to the front
        if self.size == self.limit:
            del self.storage[self.order.head.value[0]]
            self.order.remove_from_head()
            self.size -= 1
    # if it's not in the cache, add to the front of the cache
        self.order.add_to_tail((key, value))
        self.storage[key] = self.order.tail
        self.size += 1



