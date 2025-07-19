# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def recursive_serialize(root):
            if root == None:
                return '#'
            else:
                left = recursive_serialize(root.left)
                right = recursive_serialize(root.right)
                return str(root.val) + ',' + left + ',' + right

        return recursive_serialize(root)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def recursive_deserialize(data_list):
            val = next(data_list)
            if val == "#":
                return None
            else:
                root = TreeNode(int(val))
                root.left = recursive_deserialize(data_list)
                root.right = recursive_deserialize(data_list)

                return root

        if data == "":
            return None

        data_list = iter(data.split(","))
        return recursive_deserialize(data_list)
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
