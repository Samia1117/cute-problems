# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None:
            return False
        
        # current = head
        # seen = []
        # while (current != None):
        #     if current in seen:
        #         return True
        #     seen.append(current)
        #     current = current.next
        
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            # if cycle exsits, fast will catch up slow, fast will never reach end/None
            if fast == slow:
                return True
        return False
            
        return False
            
        
