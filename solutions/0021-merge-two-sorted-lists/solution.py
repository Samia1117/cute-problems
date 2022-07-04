# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        # keep two pointers, start with the heads of the list
        # compare head1 to head2 -> 
        # if head1 is smaller than head2 -> 
        # make head1 the head and move head1 forward
        # else make head2 the head and move head2 forward
        
        if list1 == None and list2!=None:
            return list2
        elif list2 == None and list1!=None:
            return list1
        elif list1 == None and list2==None:
            return None
        else:   # neither None
            head = None
            if list1.val<=list2.val:
                head = list1
                list1 = list1.next
            elif list2.val<list1.val:
                head = list2
                list2 = list2.next
            
            headPtr = head
            # print("current headPtr: ", headPtr.val)
            while (list1!=None and list2!=None):
                if list1.val<=list2.val:
                    headPtr.next = list1
                    list1 = list1.next
                    headPtr = headPtr.next
                    
                elif list2.val<list1.val:
                    headPtr.next = list2
                    list2 = list2.next
                    headPtr = headPtr.next 
                    
                # print("current headPtr: ", headPtr.val)

            if list1!=None:
                while (list1 !=None):
                    headPtr.next = list1
                    list1 = list1.next
                    headPtr = headPtr.next
                    # print("current headPtr: ", headPtr.val)
            
            elif list2!=None:
                while (list2 !=None):
                    headPtr.next = list2
                    list2 = list2.next
                    headPtr = headPtr.next
                    # print("current headPtr: ", headPtr.val)
                
        return head
                    
                    
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
        
