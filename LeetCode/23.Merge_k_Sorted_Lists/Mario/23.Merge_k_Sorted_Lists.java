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
    public ListNode mergeKLists(ListNode[] lists) {
        int n = lists.length - 1;
        if (n < 0) {
            return null;
        }
        return mergeLists(lists, 0, n / 2, n);
    }

    private ListNode mergeLists(ListNode[] lists, int s, int m, int e) {
        // end condition
        if (s == e) {
            return lists[s];
        }

        // divide
        int l = (s + m) / 2;
        ListNode left = mergeLists(lists, s, l, m);
        int r = (m + 1 + e) / 2;
        ListNode right = mergeLists(lists, m + 1, r, e);

        // conquer
        ListNode dummy = new ListNode();
        ListNode node = dummy;
        ListNode lp = left;
        ListNode rp = right;

        while (lp != null && rp != null) {
            if (lp.val < rp.val) {
                node.next = lp;
                lp = lp.next;
            } else {
                node.next = rp;
                rp = rp.next;
            }
            node = node.next;
        }

        if (lp != null) {
            node.next = lp;
        }

        if (rp != null) {
            node.next = rp;
        }

        return dummy.next;
    }
}