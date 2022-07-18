# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def findHeight(self, root, currentHeight):
        #print("Current height now: ", currentHeight)
        #print("root is: ", root)
        if root == None:
            #print("returning current height= ", currentHeight)
            return currentHeight
        else:
            return max(
                self.findHeight(root.right, currentHeight+1), self.findHeight(root.left, currentHeight+1) )
            
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        if root == None:
            return True
        
        rightHeight = self.findHeight(root.right, 0)
        #print("right is; ", rightHeight)
        leftHeight = self.findHeight(root.left, 0)
        #print("left is; ", leftHeight)
        
        if abs(rightHeight-leftHeight)>1:
            return False
        
        rightIsBalanced = self.isBalanced(root.right)
        leftIsBalanced = self.isBalanced(root.left)
        
        return rightIsBalanced and leftIsBalanced

