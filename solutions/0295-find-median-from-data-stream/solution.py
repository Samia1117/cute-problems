import heapq 

class MedianFinder:

    def __init__(self):

        self.size = 0

        max_heap = []
        min_heap = []
        heapq.heapify(max_heap)
        heapq.heapify(min_heap)

        self.max_heap = max_heap
        self.min_heap = min_heap

    def addNum(self, num: int) -> None:
        self.size += 1
        # max heap keeps track of the smaller half of the data
        heapq.heappush(self.max_heap, -num) # large negative numbers (i.e. max data vals) will be at top

        # min heap keeps track of the larger half of the data
        # now we are moving the large negative val (in its positive format) to the min_heap
        heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))

        if len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
        
    def findMedian(self) -> float:
        if self.size % 2 == 1: 
            # odd
            return -self.max_heap[0]
        else:
            return (self.min_heap[0] -self.max_heap[0]) / 2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
