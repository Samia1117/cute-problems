/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        
        if (head == null) {
            return head;
        }
        int listSize = 0;
        ListNode headPtr = head;
        while (head != null) {
            head = head.next;
            listSize ++;
        }
        System.out.println("Size of linked list = " + listSize);

        // n >= 1 so if listSize == 1, we remove the only element available in the list
        if (listSize == 1) {
            return null;
        }

        // head to return, unless we remove the head itself - special case treated separately
        ListNode headPtr2 = headPtr;
        // reframing the indexToRemove from the start instead of from the end
        int indexToRemove = listSize - n;
        System.out.println("indexToRemove = " + indexToRemove);

        int i = 0;
        ListNode prev = null;
        while(headPtr != null) {
            // stop when you hit the index before indexToRemove
            if (i == indexToRemove) {
                if (prev == null) {
                    return headPtr.next;
                } else {
                    prev.next = headPtr.next;
                    break;
                }
            }
            prev = headPtr;
            headPtr = headPtr.next;
            i += 1;
        }
        return headPtr2;
    }
}
