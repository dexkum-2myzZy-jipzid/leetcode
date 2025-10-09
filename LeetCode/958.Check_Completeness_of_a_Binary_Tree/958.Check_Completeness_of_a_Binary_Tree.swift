/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public var val: Int
 *     public var left: TreeNode?
 *     public var right: TreeNode?
 *     public init() { self.val = 0; self.left = nil; self.right = nil; }
 *     public init(_ val: Int) { self.val = val; self.left = nil; self.right = nil; }
 *     public init(_ val: Int, _ left: TreeNode?, _ right: TreeNode?) {
 *         self.val = val
 *         self.left = left
 *         self.right = right
 *     }
 * }
 */
class Solution {
    func isCompleteTree(_ root: TreeNode?) -> Bool {
        guard let root = root else { return true }

        var q: [TreeNode?] = [root], head = 0
        var seenNil = false

        while head < q.count {
            let node = q[head]
            head += 1

            if node == nil {
                seenNil = true
            } else {
                // current node is not nil, it should be nil
                if seenNil { return false }

                q.append(node!.left)
                q.append(node!.right)
            }
        }

        return true
    }
}
