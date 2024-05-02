import time

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

    def get(self, key: int) -> int:
        cache = self.cache
        if key in cache:
            # update this key's last updated time
            self.cache[key] = (cache[key][0], time.time())
            return cache[key][0]
        return -1

    def put(self, key: int, value: int) -> None:
        # print("cache: ", self.cache)
        cache = self.cache
        if key in cache:
            self.cache[key] = (value, time.time())
        else:
            # new key
            if len(cache) < self.capacity:
                self.cache[key] = (value, time.time())
            else:
                # print("resizing at cache length, cap = ", [len(cache), self.capacity])
                # evict the least recently used key
                oldest_time = sys.maxsize
                oldest_key = None
                for k in cache:
                    if cache[k][1] < oldest_time:
                        oldest_key = k
                        oldest_time = cache[k][1]

                self.cache.pop(oldest_key)
                self.cache[key] = (value, time.time())


        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
