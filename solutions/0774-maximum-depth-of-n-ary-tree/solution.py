"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
       # recursive approach
#         if not root:
#             return 0

#         maxDepth = 0
#         for ch in root.children:
#             depth = self.maxDepth(ch)
#             #print("depth for child={} is {} ".format(ch.val, depth))
#             if depth>maxDepth:
#                 maxDepth = depth
                
#         return maxDepth +1 
        
    # 
        if not root:
            return 0
        q = deque([root])
        depth = 0
        while q:
            level = len(q)
            for i in range(level):
                parent = q.popleft()
                for child in parent.children:
                    q.append(child)
            depth +=1
        return depth
        
