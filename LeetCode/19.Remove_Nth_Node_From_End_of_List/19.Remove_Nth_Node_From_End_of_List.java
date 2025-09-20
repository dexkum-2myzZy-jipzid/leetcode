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
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode dummy = new ListNode(-1);
        dummy.next = head;
        ListNode node = dummy;

        int len = 0;
        while (node.next != null) {
            len += 1;
            node = node.next;
        }

        if (len < n) {
            return head;
        } else if (len == n) {
            return head.next;
        }

        ListNode fast = dummy, slow = dummy;

        int i = 0;
        while (i < n && fast.next != null) {
            i += 1;
            fast = fast.next;
        }

        while (fast.next != null) {
            fast = fast.next;
            slow = slow.next;
        }

        slow.next = slow.next.next;

        return dummy.next;
    }
}