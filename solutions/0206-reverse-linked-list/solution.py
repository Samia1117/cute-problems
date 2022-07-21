# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return head
        
        prevNode = None
        headPtr = head
        
        while head!= None:
            nextNode = head.next
            head.next = prevNode
            
            prevNode = head
            head = nextNode
        
        return prevNode
            
