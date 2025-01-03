# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def level_search(self, node, depth, hmap): 
        if not node:
            return
        
        if depth not in hmap:
            hmap[depth] = []
        hmap[depth].append(node.val)

        if node.left != None:
            self.level_search(node.left, depth+1, hmap)
        
        if node.right != None:
            self.level_search(node.right, depth+1, hmap)

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # find nodes at same level
        # only output the node to the rightmost place on that level
        # kind of like the most "positive" node, if going left meant a -1 and going right was a +1

        hmap = {}
        self.level_search(root, 0, hmap)
        # print("hmap = ", hmap)

        ret = [x[-1] for x in hmap.values()]
        # print("ret = ", ret)
        return ret


        
