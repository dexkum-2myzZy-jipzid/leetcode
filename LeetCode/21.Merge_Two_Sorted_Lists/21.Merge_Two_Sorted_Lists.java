/**
 * Definition for singly-linked list.
 * public class ListNode {
 * int val;
 * ListNode next;
 * ListNode() {}
 * ListNode(int val) { this.val = val; }
 * ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode dummy = new ListNode();

        ListNode n = dummy, n1 = list1, n2 = list2;
        while (n1 != null && n2 != null) {
            if (n1.val <= n2.val) {
                n.next = n1;
                n1 = n1.next;
                n = n.next;
            } else {
                n.next = n2;
                n2 = n2.next;
                n = n.next;
            }
        }

        if (n1 != null) {
            n.next = n1;
        }

        if (n2 != null) {
            n.next = n2;
        }

        return dummy.next;
    }
}