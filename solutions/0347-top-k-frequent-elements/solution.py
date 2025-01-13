import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hmap = {}

        for num in nums:
            if num not in hmap:
                hmap[num] = 0
            hmap[num] += 1
        
        # print(f'hmap={hmap}')

        k_heap = []
        heapq.heapify(k_heap)

        for item in hmap.items():
            # for each item, push the item into the heap
            # if heap size exceeds 'k', pop an item off

            heappush(k_heap, (item[1], item[0]) )
            if len(k_heap) > k:
                heappop(k_heap)
        
        # print(f'K heap = {k_heap}')
        return [x[1] for x in k_heap]

        
