# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    
    def serializeRec(self, root, nodes_list):
        if not root:
            nodes_list.append('#')
            return

        nodes_list.append(str(root.val))
        self.serializeRec(root.left, nodes_list)
        self.serializeRec(root.right, nodes_list)

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """

        nodes_list = []
        self.serializeRec(root, nodes_list)
        return ','.join(nodes_list)

    def deserializeRec(self, data_list, list_int):
        curr_idx = list_int[0]
        # print(f'curr_index = {curr_idx}')

        if data_list[curr_idx] == "#":
            list_int[0] += 1
            return None

        root = TreeNode(int(data_list[curr_idx]))
        list_int[0] += 1

        root.left = self.deserializeRec(data_list, list_int)
        root.right = self.deserializeRec(data_list, list_int)

        return root

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        int_list = [0]
        data_list = data.split(',')
        return self.deserializeRec(data_list, int_list)
        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
