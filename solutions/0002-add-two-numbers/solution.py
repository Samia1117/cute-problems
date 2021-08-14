# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]: 
        carry = 0
        l3 = ListNode(val=0)
        pointer = l3
        while l1!= None or l2!=None:
            #print("l1.val, l2.val: ", l1.val, l2.val)
            sum = carry  
            if l1 != None:
                sum += l1.val
                l1 = l1.next
            if l2 != None:
                sum += l2.val
                l2 = l2.next
                
            carry = sum//10
            l3.val = sum%10
            if l1== None and l2==None:
                if carry>0:
                    l3.next = ListNode(val=carry)
                break
            l3.next = ListNode(val=0)
            l3 = l3.next
            
        
        return pointer
            
