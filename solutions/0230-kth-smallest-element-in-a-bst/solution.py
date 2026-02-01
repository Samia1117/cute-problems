from heapq import heapify, heappush, heappop

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # traverse the binary tree and gather all the values in an array
        # or maybe just store a k-heap and pop off values if heap_size > k

        def _dfs(root: Optional[TreeNode], k_heap: list) -> None:

            if not root:
                return
            # k_heap.append(root.val)
            heappush(k_heap, -root.val)

            _dfs(root.left, k_heap)
            _dfs(root.right, k_heap)
            # if len(k_heap) > k:
            #     heappop(k_heap)
        
        heap = []
        _dfs(root, heap)

        n = len(heap)
        for i in range(n-k):
            heappop(heap)
        # print(f'heap = {heap}')
        return heap[0] * -1
        
