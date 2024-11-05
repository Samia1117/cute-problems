"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    visited = {}

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        if head == None:
            return head

        if head in self.visited:
            return self.visited[head]

        new_head = Node(head.val)
        self.visited[head] = new_head

        new_head.next = self.copyRandomList(head.next)
        new_head.random = self.copyRandomList(head.random)

        return new_head
        

        
