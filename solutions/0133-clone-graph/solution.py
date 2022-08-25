"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        if not node:
            return node
        
        q = deque([node])
        copies = {node.val: Node(node.val, [])}
        
        while q:
            popped = q.popleft()
            copy = copies[popped.val]
            
            for neigh in popped.neighbors:
                if neigh.val not in copies:
                    copies[neigh.val] = Node(neigh.val, [])
                    q.append(neigh)
                    
                copy.neighbors.append(copies[neigh.val])
        
        return copies[node.val]
    
#         q = deque()
#         q.append(node)
#         discovered = set()
#         discovered.add(node.val)
        
#         root = Node(node.val, [])
#         q2 = deque()
#         q2.append(root)
        
#         seenNodes = {}
#         seenNodes[node.val] = root
        
#         while q:
#             popped = q.popleft()
#             popped2 = q2.popleft()
            
#             for neighbor in popped.neighbors:
#                 try:
#                     existingNode = seenNodes[neighbor.val]
#                     popped2.neighbors.append(existingNode)
#                 except KeyError:
#                     copy = Node(neighbor.val)
#                     popped2.neighbors.append(copy)
#                     seenNodes[neighbor.val] = copy
                
#                 if neighbor.val not in discovered:
#                     q.append(neighbor)
#                     q2.append(copy)
                    
#                 discovered.add(neighbor.val)
                
#         return root
                
                
                
                
                
