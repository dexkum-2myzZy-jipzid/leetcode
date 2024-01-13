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
    public ListNode sortList(ListNode head) {
        if (head == null || head.next == null) {
            return head;
        }

        // split two list
        ListNode right = getMid(head);
        ListNode left = head;
        ListNode tmp = right.next;
        right.next = null;
        right = tmp;

        left = sortList(left);
        right = sortList(right);

        return merge(left, right);
    }

    private ListNode getMid(ListNode head) {
        ListNode fast = head.next;
        ListNode slow = head;
        while (fast != null && fast.next != null) {
            fast = fast.next.next;
            slow = slow.next;
        }
        return slow;
    }

    private ListNode merge(ListNode left, ListNode right) {
        ListNode dummy = new ListNode();
        ListNode node = dummy;

        while (left != null && right != null) {
            if (left.val > right.val) {
                node.next = right;
                right = right.next;
            } else {
                node.next = left;
                left = left.next;
            }
            node = node.next;
        }

        if (left != null) {
            node.next = left;
        }

        if (right != null) {
            node.next = right;
        }

        return dummy.next;
    }

}