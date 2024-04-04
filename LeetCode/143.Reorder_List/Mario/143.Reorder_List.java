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
    public void reorderList(ListNode head) {

        // handle corner case
        if (head.next == null)
            return;

        // find middle point
        ListNode fast = head, slow = head;
        while (fast != null) {
            fast = fast.next != null ? fast.next.next : fast.next;
            slow = slow.next;
        }

        // reverse later part
        ListNode pre = null, cur = slow, next = null;
        while (cur != null) {
            next = cur.next;
            cur.next = pre;
            pre = cur;
            cur = next;
        }
        cur = pre;

        // merge
        // dump -> 1,2
        // cur -> 4. 3
        ListNode dump = head;
        while (cur != null) {
            ListNode next1 = dump.next;
            dump.next = cur;
            ListNode next2 = cur.next;
            cur.next = next1;
            cur = next2;
            dump = next1;
        }
        dump.next = null;
    }
}