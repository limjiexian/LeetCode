class Node:
    def __init__(self, key, val, next=None, prev=None):
        self.key, self.val = key, val
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.least = Node(0, 0)
        self.most = Node(0, 0)

        self.least.next = self.most
        self.most.prev = self.least

        self.cache = {}
        self.cap = capacity

    def remove(self, node):
        prev, nex = node.prev, node.next
        prev.next, nex.prev = nex, prev


    def insert(self, node):
        # l <- mid -> r
        mid = self.most.prev
        mid.next = node
        node.next = self.most
        node.prev = mid
        self.most.prev = node


    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])

            return self.cache[key].val
        return -1
        
    def put(self, key: int, value: int) -> None:
        # key already exist
        # just remove it from LRU, create updated cache key:value node, insert back to LRU
        if key in self.cache:
            self.remove(self.cache[key])
            self.cache[key] = Node(key, value)
            self.insert(self.cache[key])
        else:
            # if key dont exist
            # create the node and store in cache
            # then insert into LRU doubly ll
            # check if we exceeded capacity, if so then just remove, else do nth
            self.cache[key] = Node(key, value)
            self.insert(self.cache[key])

            if len(self.cache) > self.cap:
                target_key = self.least.next.key
                self.remove(self.cache[target_key])
                del self.cache[target_key]



        
