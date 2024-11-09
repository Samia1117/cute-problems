"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:

    visited = {}

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node:
            return None
        
        if node in self.visited:
            return self.visited[node]
        
        new_node = Node(node.val)
        self.visited[node] = new_node

        new_neighbors = []
        for n in node.neighbors:
            new_neighbor = self.cloneGraph(n)
            new_neighbors.append(new_neighbor)
        
        new_node.neighbors = new_neighbors

        return new_node
        

        
