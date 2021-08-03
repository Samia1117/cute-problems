# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getPaths(self, root: TreeNode, target: int, runningPath: List[int], paths: List[List[int]]) -> None:
        if root == None:
            return
        if root.right == None and root.left==None:
            if root.val == target:
                foundPath = runningPath + [root.val]
                paths.append(foundPath)
            return
        
        self.getPaths(root.left, target-root.val, runningPath + [root.val], paths)
        self.getPaths(root.right, target-root.val, runningPath + [root.val], paths)
        return
        
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        
        if root == None:
            return []
        all_paths = []
        runningPath = []
        
        self.getPaths(root, targetSum, runningPath, all_paths)
        print(all_paths)
        
        #res = []
        # for path in all_paths:
        #     if sum(path) == targetSum:
        #         res.append(path)
                
        return all_paths
            
