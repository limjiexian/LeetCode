class Node:
    def __init__(self, key, val):
        self.val = val
        self.key = key
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} # map to key to node    // key: node

        self.left = Node(0, 0)
        self.right = Node(0, 0)

        self.left.next = self.right
        self.right.prev = self.left

    def get(self, key: int) -> int:
        # check if inside else return -1
        if key in self.cache:
            # since we accessed it aka must update the priority
            self.remove(self.cache[key]) 
            self.insert(self.cache[key]) # to the right most

            return self.cache[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        # check if key is already in cache
        # if already in, we want to remove the key node, and later re insert
        if key in self.cache:
            self.remove(self.cache[key])
        
        # regardless of whether the key alr exist in the cache, we need create a new Node with the updated key, value pair and store into the cache
        # this is because, key: value, the value can change over time so we need update it
        self.cache[key] = Node(key, value)  # cr8 and store in cache
        self.insert(self.cache[key])        # cr8 and store priority in our doubly linkedlist
        
        # check if capacity is hit
        if len(self.cache) > self.cap:
            # remove LRU
            # get the LRU node first
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

    def remove(self, node: Node):
        prev, nxt = node.prev, node.next

        nxt.prev = prev
        prev.next = nxt
    
    def insert(self, node: Node):
        prev = self.right.prev
        nxt = self.right

        # connect prev node to new node
        prev.next = node
        node.prev = prev # new node prev connect to prev node

        # connect new node to self.right node
        node.next = nxt
        nxt.prev = node




    
