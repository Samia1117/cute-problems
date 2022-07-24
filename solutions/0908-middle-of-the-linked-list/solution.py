# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
#         if head == None:
#             return None
        
#         head2 = head
        
#         count = 0
#         while head!=None:
#             head = head.next
#             count +=1
#             # print("head is: ", head)
#             # print("count is: ", count)
        
#         mid = count//2 # 6//2 = 3, 5//2 = 2
        
#         count2 = 0
#         while count2!=mid:
#             head2 = head2.next
#             count2 +=1
            
#         return head2

        slow = head
        fast = head
        
        while fast and fast.next: 
            slow = slow.next
            fast = fast.next.next

        return slow
