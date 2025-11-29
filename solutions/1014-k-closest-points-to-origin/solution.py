# from collections import heapq

class Node:
    def __init__(self, dist, point):
        self.dist = dist
        self.point = point

    def __lt__(self, other):
        return self.dist > other.dist

    def __repr__(self):
        return f'{self.dist}, ({self.point})'

class Solution:
    
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        '''
        One idea is to create a map of (x,y) from their distance to origin
        Sort the dictionary by key and return top k values

        Keep a size-k heap, so that runtime will be worst case O(nlogk)
        Good for a first time attempt, before thinking further
        '''
        
        heap = []
        heapq.heapify(heap)
        heap_size = 0

        for point in points:
            x, y = point[0], point[1]
            orig_dist = (x**2 + y**2)**0.5
            node = Node(orig_dist, (x, y))
            print(f'Node = {node}')

            heapq.heappush(heap, node)
            heap_size += 1
            if heap_size > k:
                heapq.heappop(heap)
        
        # print(f'Heap (size = {len(heap)}) elts in order...')
        
        ret = []
        while heap:
            elt = heapq.heappop(heap)
            x, y = elt.point[0], elt.point[1]
            # print(f'Next elt = ({elt})')
            ret.append([x, y])
        
        return ret[::-1]
        
