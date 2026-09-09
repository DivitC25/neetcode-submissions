class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.size = 0
        self.timestamp = 0
        self.usage = {}
        

    def get(self, key: int) -> int:
        if key in self.cache:
            self.usage[key] = self.timestamp
            self.timestamp += 1
            return self.cache[key]
        else:
            self.timestamp += 1
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key] = value
            self.usage[key] = self.timestamp
            self.timestamp += 1
        else:
            if self.size < self.capacity:
                self.cache[key] = value
                self.usage[key] = self.timestamp
                self.size += 1
                self.timestamp += 1
            else:
                oldestKey = min(self.usage.keys(), key = lambda x: self.usage[x])
                self.cache.pop(oldestKey)
                self.usage.pop(oldestKey)
                self.cache[key] = value
                self.usage[key] = self.timestamp
                self.timestamp += 1


            
        
