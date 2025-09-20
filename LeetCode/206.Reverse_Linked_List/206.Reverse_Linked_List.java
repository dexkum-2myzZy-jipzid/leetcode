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
    public ListNode reverseList(ListNode head) {
        // node2 is a new list
        ListNode node1 = head, node2 = null;

        while (node1 != null) {
            ListNode tmp = node1.next;
            node1.next = node2;
            node2 = node1;
            node1 = tmp;
        }

        return node2;
    }
}