/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public var val: Int
 *     public var next: ListNode?
 *     public init() { self.val = 0; self.next = nil; }
 *     public init(_ val: Int) { self.val = val; self.next = nil; }
 *     public init(_ val: Int, _ next: ListNode?) { self.val = val; self.next = next; }
 * }
 */
class Solution {
    func mergeTwoLists(_ list1: ListNode?, _ list2: ListNode?) -> ListNode? {
        let dummy = ListNode(-1)
        var cur: ListNode? = dummy
        var l1: ListNode? = list1, l2: ListNode? = list2

        while let a = l1, let b = l2 {
            if a.val <= b.val {
                cur?.next = a
                l1 = a.next
            } else {
                cur?.next = b
                l2 = b.next
            }
            cur = cur?.next
        }

        cur?.next = l1 ?? l2

        return dummy.next
    }
}
