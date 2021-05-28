# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    
    def reverse_linkedlist(self, head):
        prevNode = None
        nextNode = None
        currentNode = head
        while (currentNode!= None):
            nextNode = currentNode.next
            currentNode.next = prevNode
            prevNode = currentNode
            currentNode = nextNode   # at the end, null
        return [prevNode, currentNode]
    
    def reverse_linkedlist_k(self, head, k):
        prevNode = None
        nextNode = None
        currentNode = head
        i = 1   # number of reversals done so far
        while (currentNode!= None and i<=k):
            nextNode = currentNode.next
            currentNode.next = prevNode
            prevNode = currentNode
            currentNode = nextNode   # at the end, null
            i+=1
            if currentNode == None and i<=k and i>1:
                prev, current = self.reverse_linkedlist(prevNode) 
                return [prev, current]
        return [prevNode, currentNode]
    
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        
        final_head = None
        lastNode = 0
        lastLink = None
        while lastNode !=None:
            results = self.reverse_linkedlist_k(head, k)
            rev_head = results[0]
            if lastLink !=None:  # lastlink is the last node of a reversed group
                lastLink.next = rev_head    # link it to first node of next reversed group
            else:           
                final_head = rev_head
            while rev_head!= None:
                if rev_head.next == None:  
                    lastLink = rev_head 
                rev_head = rev_head.next
            lastNode = results[1]
            head = lastNode
        return final_head
    
    
