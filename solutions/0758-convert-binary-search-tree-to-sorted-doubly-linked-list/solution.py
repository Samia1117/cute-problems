"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    class GlobalVal:
        def __init__(self):
            self.val = None
    def findNext(self, root):
        if root == None:
            return root
        if root.left != None:
            l = self.findNext(root.left)
            root.left = l
            l.right = root
        if root.right != None:
            r = self.findNext(root.right)
            r2 = r
            while r.left != None:
                r = r.left
            r.left = root
            root.right = r
            return r2
        return root
            
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        ll = self.findNext(root)
        lastnode = ll
        firstnode = None
        while ll != None:
            #print(ll.val)
            if ll.left == None:
                firstnode = ll
                #print("first node is: ", ll.val)
                #print("first node has right: ", firstnode.right)
                firstnode.left = lastnode
                lastnode.right= firstnode
                break
            ll = ll.left
            
        return firstnode
            
        
        
