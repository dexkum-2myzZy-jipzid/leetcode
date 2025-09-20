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
    public boolean isPalindrome(ListNode head) {
        // 1->2->3->4
        // get half end
        ListNode dummy = new ListNode(-1);
        dummy.next = head;
        ListNode slow = dummy, fast = dummy;
        while (fast != null) {
            slow = slow.next;

            fast = fast.next;
            if (fast != null) {
                fast = fast.next;
            }
        }

        // reverse half end linkedlist
        ListNode other = null;
        while (slow != null) {
            ListNode tmp = slow.next;
            slow.next = other;
            other = slow;
            slow = tmp;
        }

        // compare it
        ListNode cur = dummy.next;
        while (other != null && cur != null) {
            if (other.val != cur.val) {
                return false;
            } else {
                other = other.next;
                cur = cur.next;
            }
        }

        return true;
    }
}