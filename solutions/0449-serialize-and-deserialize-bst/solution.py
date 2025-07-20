# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        def rserialize(node):
            if not node:
                return "#"
            left = rserialize(node.left)
            right = rserialize(node.right)
            # print(f'left, right = {left, right}')
            return str(node.val) + "," + left + "," + right

        data_str = rserialize(root)
        print(f'data_str = {data_str}')
        return data_str
        

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        def rserialize(data_list, index):
            if index[0] == len(data_list):
                print("Problem")
                return None
            if data_list[index[0]] == "#":
                index[0] += 1
                return None
            
            root_node = TreeNode(int(data_list[index[0]]))
            index[0] += 1
            root_node.left = rserialize(data_list, index)
            root_node.right = rserialize(data_list, index)
            
            return root_node
        
        root = rserialize(data.split(","), [0])
        return root
        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
