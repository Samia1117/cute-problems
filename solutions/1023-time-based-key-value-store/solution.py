from bisect import bisect_right
class TimeMap:
    def __init__(self):
        self.timemap = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:

        if key not in self.timemap:
            self.timemap[key] = [[], []] # parallel lists (timestamps, values)

        self.timemap[key][0].append(timestamp)
        self.timemap[key][1].append(value)

    def get(self, key: str, timestamp: int) -> str:
        
        if key not in self.timemap:
            return ""

        timestamps = self.timemap[key][0]
        values = self.timemap[key][1]

        # find the first index where this timestamp could be inserted keeping the timestamp order
        index = bisect_right(timestamps, timestamp)
        if index == 0:
            return ""
        
        return values[index-1]



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
