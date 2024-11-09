# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        if not head:
            return None

        # 1. find mid point of list
        slow = head
        fast = head
        last = head
        while fast!= None and fast.next != None:
            fast = fast.next.next
            if not fast or not fast.next:
                last = slow
                slow = slow.next
            else:
                slow = slow.next
        
        last.next = None
        mid = slow

        # 2. Create a copy of the linked list - in reverse
        curr_node = mid
        prev_node = None
        n = 0
        while curr_node != None:
            n += 1
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node

            if next_node != None:
                curr_node = next_node
            else:
                break

        rev_head = curr_node
        head_ptr = head

        # head_itr = head
        # rev_head_itr = rev_head
        # print("Printing reverse list...")
        # while rev_head_itr != None:
        #     print("next = ", rev_head_itr.val)
        #     rev_head_itr = rev_head_itr.next

        # print("Printing original list...")
        # while head_itr != None:
        #     print("next = ", head_itr.val)
        #     head_itr = head_itr.next
        # merge the two lists

        while rev_head and head:
            rev_head_next = rev_head.next
            head_next = head.next

            head.next = rev_head
            if head_next == None and rev_head_next != None:
                rev_head.next = rev_head_next
            else:
                rev_head.next = head_next

            head = head_next
            rev_head = rev_head_next

        return head_ptr


        
