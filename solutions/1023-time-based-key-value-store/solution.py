class TimeMap:

    def __init__(self):
        self.map = {}
    
    def binarySearchLargestTime(self, tups, timestamp):
        l = 0
        r = len(tups)-1
        mid = (l+r)//2
        maxVal = ""
        while l!=mid:
            if tups[mid][0] < timestamp:
                l = mid
                maxVal = tups[mid][1]
            elif tups[mid][0] > timestamp:
                r = mid
            else:
                return timestamp
            mid = (l+r)//2
            
        if tups[r][0]<=timestamp:
            return tups[r][1]
        if tups[l][0]<=timestamp:
            return tups[l][1]
        return ""

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = []
        self.map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        
        if key not in self.map:
            return ""
            #raise Exception("key is not in map")
        
        # shrunk = list(filter(lambda x: x[0]<=timestamp, self.map[key]))
        return self.binarySearchLargestTime(self.map[key], timestamp)
    
        if len(shrunk)==0:
            return ""
        # sortedtups = sorted(shrunk, key=lambda x: x[0])
        # return sortedtups[-1][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
