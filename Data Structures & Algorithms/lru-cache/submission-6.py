class Node:
    def __init__(self,key,value):
        self.key,self.value = key,value 
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity

        self.left = Node(0,0)
        self.right = Node(0,0)

        self.left.next = self.right 
        self.right.prev = self.left 

        self.cache = {}

    def remove(self,node):
        node.prev.next = node.next
        node.next.prev = node.prev 

    def insert(self,node):
        node.prev = self.right.prev 
        self.right.prev.next = node 
        self.right.prev = node
        node.next = self.right 
    
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value 
        return -1 

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].value = value 
            self.remove(self.cache[key])
            self.insert(self.cache[key])
        if key not in self.cache:
            new_node = Node(key,value)
            self.insert(new_node)
            self.cache[key] = new_node 
        if len(self.cache) > self.capacity:
            lru = self.left.next 
            self.remove(lru)
            del self.cache[lru.key]
