/**
 * Definition for a Node.
 * public class Node {
 *     public var val: Int
 *     public var left: Node?
 *     public var right: Node?
 *     public var parent: Node?
 *     public init(_ val: Int) {
 *         self.val = val
 *         self.left = nil
 *         self.right = nil
 *         self.parent = nil
 *     }
 * }
 */

class Solution {
    func lowestCommonAncestor(_ p: Node?, _ q: Node?) -> Node? {
        // a: 5 -> 3 -> 4 -> 2 -> 5
        // b: 4 -> 2 -> 5 -> 3 -> 5
        guard let p = p, let q = q else { return nil }

        if p === q { return p }

        var a: Node? = p, b: Node? = q
        while a !== b {
            a = a?.parent ?? q
            b = b?.parent ?? p
        }

        return a
    }
}
