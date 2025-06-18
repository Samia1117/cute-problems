class ListNode:
    def __init__(self, key, val):
        self.prev = None
        self.next = None
        self.key = key
        self.val = val

class LRUCache:

    '''
    Add node to the front (tail) of the linkedlist
    '''
    def add(self, node):
        # pass
        prev_end = self.tail.prev
        prev_end.next = node
        node.prev = prev_end
        node.next = self.tail
        self.tail.prev = node

    '''
    Remove node from ll
    '''
    def remove(self, node):
        prev = node.prev
        nex = node.next

        if prev != None:
            prev.next = nex
        if nex != None: 
            nex.prev = prev

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = ListNode(-1, -1)
        self.tail = ListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        # remove it from its prev position in ll
        self.remove(node)
        # now make it MRU
        self.add(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        # if key already in cache, then update; else add to tail
        # if exceed capacity, first remove tail

        if key in self.cache:
            # update
            node = self.cache[key]
            self.remove(node)
        
        # add this node to cache and to inner linked list
        node = ListNode(key, value)
        self.cache[key] = node
        self.add(node)

        if len(self.cache) > self.capacity:
            # remove head 
            lru_node = self.head.next
            self.remove(lru_node)
            del self.cache[lru_node.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
