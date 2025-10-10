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
    func mergeKLists(_ lists: [ListNode?]) -> ListNode? {
        guard !lists.isEmpty else { return nil }
        // divide & conquer
        let l = 0, r = lists.count - 1

        return helper(l, r)

        func helper(_ l: Int, _ r: Int) -> ListNode? {
            guard l <= r else { return nil }
            if l == r { return lists[l] }

            let m = (l + r) /2
            let left = helper(l, m), right = helper(m + 1, r)

            // merge left and right linked list
            return merge(left, right)
        }

        func merge(_ l: ListNode?, _ r: ListNode?) -> ListNode? {
            var l = l, r = r

            let dummy = ListNode(-1)
            var cur: ListNode? = dummy

            while let left = l, let right = r {
                if left.val <= right.val {
                    cur?.next = left
                    l = left.next
                } else {
                    cur?.next = right
                    r = right.next
                }
                cur = cur?.next
            }

            cur?.next = l ?? r

            return dummy.next
        }
    }
}

// heap
extension ListNode: Comparable {
    public static func < (lhs: ListNode, rhs: ListNode) -> Bool {
        lhs.val < rhs.val
    }

    public static func == (lhs: ListNode, rhs: ListNode) -> Bool {
        lhs.val == rhs.val
    }
}

class Solution {
    func mergeKLists(_ lists: [ListNode?]) -> ListNode? {
        var heap = Heap<ListNode>()
        for list in lists {
            if let node = list {
                heap.insert(node)
            }
        }

        let dummy = ListNode(-1)
        var cur: ListNode? = dummy

        while let node = heap.popMin() {
            cur?.next = node
            cur = cur?.next
            if let next = node.next {
                heap.insert(next)
            }
        }
        cur?.next = nil

        return dummy.next
    }
}
