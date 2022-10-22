# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        i = 0
        headPtr = head
        while head != None:
            i +=1
            head = head.next

        checkUntil = i-n
        j = 0
        prev = None
        ret = headPtr
        while j <= checkUntil:
            # update pointers
            if j== checkUntil:
                print("got to checkUntil: ", j)
                nextNode = headPtr.next
                if prev !=None:
                    print("updating pointers to skip head = ", headPtr)
                    prev.next = nextNode
                    print("nextnode is: ", nextNode)
                    break
                else:
                    return nextNode
            prev = headPtr
            headPtr = headPtr.next
            j+=1
        
        return ret
                
            
        
        
