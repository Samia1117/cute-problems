"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':

        def flatten_rec(head: Optional[Node]) -> tuple[Optional[Node], Optional[Node]]:
            if not head:
                return None
            
            next_node = head.next # keep for reference
            tail = head
            if head.child:
                child_head = head.child

                flattened_child_tail = flatten_rec(child_head)

                head.next = child_head # next item is child head
                child_head.prev = head
                head.child = None

                if next_node:
                    flattened_child_tail.next = next_node
                    next_node.prev = flattened_child_tail

                # flatten original head.next and then point child tail to the head of that flattened list
            
            flattened_tail = flatten_rec(tail.next)
                
            return flattened_tail if flattened_tail else tail
        
        tail = flatten_rec(head)
        return head


