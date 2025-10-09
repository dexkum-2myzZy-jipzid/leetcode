/**
 * Definition for a Node.
 * public class Node {
 *     public var val: Int
 *     public var next: Node?
 *     public init(_ val: Int) {
 *         self.val = val
 *         self.next = nil
 *     }
 * }
 */

class Solution {
    func insert(_ head: Node?, _ insertVal: Int) -> Node? {
        // handle head is nil case
        let insertNode = Node(insertVal)
        guard let head = head else {
            insertNode.next = insertNode
            return insertNode
        }

        // only 1 node
        if head.next == head {
            head.next = insertNode
            insertNode.next = head
            return head
        }

        // two pointer, one is prev, one is current
        // prev.val <= insertVal < curr.val

        // prev.val > cur.val
        var prev: Node? = head.next, curr: Node? = head
        var insert = false

        while let p = prev, let c = curr {
            // prev.val > insertVal >= curr.val
            if c.val <= insertVal, insertVal < p.val {
                c.next = insertNode
                insertNode.next = p
                insert = true
                break
            }

            // insertVal >= all vals in linked list / <= all vals in linked list
            if p.val < c.val, insertVal <= p.val || insertVal >= c.val {
                c.next = insertNode
                insertNode.next = p
                insert = true
                break
            }

            prev = p.next
            curr = c.next

            if curr == head { break }
        }

        if !insert {
            curr?.next = insertNode
            insertNode.next = prev
        }

        return head
    }
}
