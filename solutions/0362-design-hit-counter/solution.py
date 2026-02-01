from bisect import bisect_right

class HitCounter:

    HITS_SINCE_SECONDS = 300
    def __init__(self):
        self.hits = []

    def hit(self, timestamp: int) -> None:
        self.hits.append(timestamp)
        
    def getHits(self, timestamp: int) -> int:
        # binary search last for the first index greater than timestamp-300
        lowest_possible_ts = timestamp-HitCounter.HITS_SINCE_SECONDS

        index = bisect_right(self.hits, lowest_possible_ts)
        # print(f'possible timestamps = {self.hits[index:]}')
        return len(self.hits) - index
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
