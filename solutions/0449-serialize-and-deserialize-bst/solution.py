# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    ser = ""
    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        # traverse the tree 
        # encode using a pre-order string

        res = []
        def rserialize(root: Optional[TreeNode]):

            if root:
                res.append(str(root.val))
                rserialize(root.left)
                rserialize(root.right)
            else:
                res.append("#")

        rserialize(root)
        return ",".join(res)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        index = [0]

        def rdeserialize(data: list[str], index: list[int]) -> Optional[TreeNode]:

            if index[0] >= len(data):
                return None

            if data[index[0]] == "#":
                index[0] += 1
                return None
            
            root = TreeNode(int(data[index[0]]))
            index[0] += 1

            root.left = rdeserialize(data, index)
            root.right = rdeserialize(data, index)

            return root
        
        return rdeserialize(data.split(","), index)


        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
