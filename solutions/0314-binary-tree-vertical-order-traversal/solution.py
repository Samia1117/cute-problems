# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:


    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        d = {}
            # d -> dictionary 
            # key = counter value
            # value = node.val for every node that has counter value = key
            # final answer is = d.values()

        def traverse(node, counter, height, d):
            # function goes here
            if node == None:
                return

            if counter not in d:
                d[counter] = []
            d[counter].append((node.val, height)) # most likely this will be the height sorted order if I traverse 

            if node.left != None:
                traverse(node.left, counter - 1 , height + 1, d)
            
            if node.right != None:
                traverse(node.right, counter + 1, height + 1, d)

            return

        if root == None:
            return []

        # d[0] = root.val
        # init counter
        counter = 0
        traverse(root, counter, 0, d)

        sort1 = sorted(list(d.keys()))

        values_in_key_order = [d[i] for i in sort1]
        # print("values_in_key_order: ", values_in_key_order)

        sorted_tup_list = [sorted(tup_list, key = lambda x: x[1]) for tup_list in values_in_key_order]
        
        # now only grab the first element in the tuple which is the node value from each list element in sorted_tup_list
        return [[tup[0] for tup in lst] for lst in sorted_tup_list]







