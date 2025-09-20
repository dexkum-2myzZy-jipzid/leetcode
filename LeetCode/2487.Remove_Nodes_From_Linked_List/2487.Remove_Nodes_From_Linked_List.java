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
    // reverse
    // 8 3 13 2 5
    // 8 13
    // 13 8
    public ListNode removeNodes(ListNode head) {
        ListNode dummy = new ListNode(-1);
        ListNode node = reverseLinkedList(head);
        dummy.next = node;
        ListNode next = node.next;
        while (next != null) {
            if (next.val >= node.val) {
                node.next = next;
                node = node.next;
            }
            next = next.next;
        }
        node.next = null;
        return reverseLinkedList(dummy.next);
    }

    private ListNode reverseLinkedList(ListNode head) {
        ListNode node = null;
        ListNode cur = head;
        while (cur != null) {
            ListNode tmp = cur.next;
            cur.next = node;
            node = cur;
            cur = tmp;
        }
        return node;
    }
}