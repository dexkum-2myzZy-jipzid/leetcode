/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public var val: Int
 *     public var next: ListNode?
 *     public init(_ val: Int) {
 *         self.val = val
 *         self.next = nil
 *     }
 * }
 */

class Solution {
    func hasCycle(_ head: ListNode?) -> Bool {
        var fast = head, slow = head

        while let f = fast, let fNext = f.next {
            slow = slow?.next
            fast = fNext.next

            if slow === fast { return true }
        }

        return false
    }
}
