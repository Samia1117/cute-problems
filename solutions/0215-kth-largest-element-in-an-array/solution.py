class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        ret = []
        heapq.heapify(ret)

        # Note: we only need to maintain a "k-heap" - it contains the k largest elements in the array 
        # Every time we pop an element from a k+1 heap, we know that the k elements within the heap are greater in
        # magnitude compared to the popped element
        # return value is the top element of the k-heap

        for num in nums:
            heapq.heappush(ret, num)

            if len(ret) > k: 
                heapq.heappop(ret)
        
        # print(f"K largest elements = {ret}")
        return heapq.heappop(ret)

            



        
