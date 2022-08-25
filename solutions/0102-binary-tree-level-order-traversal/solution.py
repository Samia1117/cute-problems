# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def dfs(self, v, depth, depthMap):
        if v==None:
            return
        if depth not in depthMap:
            depthMap[depth] = []
            
        depthMap[depth].append(v.val)
        self.dfs(v.left, depth+1, depthMap)
        self.dfs(v.right, depth+1, depthMap)
        return
    
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if root == None:
            return []
        
        dMap = {}
        self.dfs(root, 0, dMap) # the map gets populated and returned
        
#         # items = sorted(dMap.items(), key= lambda x:x[0])
#         # return [i[1] for i in items]
        return [dMap[k] for k in sorted(dMap)]
        
#         q = deque()
#         q.append(root)
#         result = []
        
#         while q:
#             nextLevel = []  
#             for i in range(len(q)):
#                 popped = q.popleft()
#                 nextLevel.append(popped.val)
                
#                 left = popped.left
#                 right = popped.right
                          
#                 if left !=None:
#                     q.append(left)
#                 if right !=None:
#                     q.append(right)
#             result.append(nextLevel)

        
#         return result
            
            
        
