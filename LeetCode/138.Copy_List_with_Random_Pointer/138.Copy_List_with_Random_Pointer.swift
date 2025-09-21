/**
 * Definition for a Node.
 * public class Node {
 *     public var val: Int
 *     public var next: Node?
 *     public var random: Node?
 *     public init(_ val: Int) {
 *         self.val = val
 *         self.next = nil
 *    	   self.random = nil
 *     }
 * }
 */

class Solution {
    func copyRandomList(_ head: Node?) -> Node? {
        guard let head = head else { return nil }

        // copy node, insert after it
        var cur: Node? = head
        while let node = cur {
            let copy = Node(node.val)
            copy.next = node.next
            node.next = copy
            cur = copy.next
        }

        // add random to copy ones
        cur = head
        while let node = cur {
            let copy = node.next
            copy?.random = node.random?.next

            cur = copy?.next
        }

        // split copy ones from orginal linked list
        // restore head linked list
        let dummy = Node(-1)
        dummy.next = head.next
        cur = head
        while let node = cur {
            let copy = node.next
            node.next = copy?.next
            cur = node.next

            copy?.next = cur?.next
        }

        return dummy.next
    }
}
