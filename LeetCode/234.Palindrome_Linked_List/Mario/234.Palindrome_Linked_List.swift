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
    func isPalindrome(_ head: ListNode?) -> Bool {
        guard let head = head, head.next != nil else { return true }

        // fast, slow pointers
        var fast: ListNode? = head, slow: ListNode? = head
        while fast != nil, fast?.next != nil {
            slow = slow?.next
            fast = fast?.next?.next
        }
        // if length of this List is odd
        if fast != nil {
            slow = slow?.next
        }

        var right = reverse(slow)
        var left: ListNode? = head

        while right != nil {
            if right?.val != left?.val {
                return false
            }
            right = right?.next
            left = left?.next
        }

        return true
    }

    private func reverse(_ node: ListNode?) -> ListNode? {
        var tail: ListNode? = nil
        var cur = node

        while let c = cur {
            let next = c.next
            c.next = tail
            tail = c
            cur = next
        }

        return tail
    }
}
