# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # traverse once to calculate size of linked list

        size = 0
        head_ptr = head
        while head != None:
            head = head.next
            size += 1
        
        if size == 1:
            return None

        k = size - n # we need kth index from the head
        if k == 0:
            return head_ptr.next
            
        head_ptr2 = head_ptr
        for i in range(k):
            if i == k-1:
                head_ptr.next = head_ptr.next.next
            else:
                head_ptr = head_ptr.next

        return head_ptr2
        
