class LRUCache:

    def __init__(self, capacity: int):
        self.lru = []
        self.capacity = capacity

    def get(self, key: int) -> int:
        for i in range(len(self.lru)):
            if self.lru[i][0] == key:
                temp = self.lru.pop(i)
                self.lru.append(temp)
                return temp[1]
        return -1

    def put(self, key: int, value: int) -> None:
        for i in range(len(self.lru)):
            if self.lru[i][0] == key:
                temp = self.lru.pop(i)
                temp[1] = value
                self.lru.append(temp)
                return 
        
        if len(self.lru) == self.capacity:
            self.lru.pop(0)
        
        self.lru.append([key,value])
        

            
