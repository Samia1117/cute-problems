# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        k = len(lists)
        if k == 0:
            return None
        
        if k == 1:
            return lists[0]
        
        ptrs = [i for i in range(k)]
        # array_lengths = [len(lst) for lst in lists]

        # ptr_to_len = {ptrs[i]:[0, array_lengths[i]] for i in range(k)}
        idx_to_node = {ptrs[i]:lists[i] for i in range(k)}

        curr_min = ListNode(sys.maxsize)
        min_index = 0
        ret = None
        ret_ptr = None

        while True:
            if not idx_to_node:
                break
            for k, v in list(idx_to_node.items()):
                if v == None:
                    del idx_to_node[k]
                    if not idx_to_node:
                        return ret_ptr
                else:
                    if v.val <= curr_min.val:
                        curr_min = v
                        min_index = k

            # print(f'idx_to_node = {[(k, v.val) for k, v in idx_to_node.items()]}')
            # print(f'min_index = {min_index}')
            if not ret:
                ret = curr_min
                ret_ptr = curr_min
            else:
                ret.next = curr_min
                ret = ret.next
            
            curr_min = ListNode(sys.maxsize)
            idx_to_node[min_index] = idx_to_node[min_index].next
           
        # print(f'ret_ptr')
        # while ret_ptr:
        #     print(ret_ptr.val)
        #     ret_ptr = ret_ptr.next

        return ret_ptr
        
