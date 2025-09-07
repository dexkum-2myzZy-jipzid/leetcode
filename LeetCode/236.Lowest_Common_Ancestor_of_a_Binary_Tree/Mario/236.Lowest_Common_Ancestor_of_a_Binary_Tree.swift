/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public var val: Int
 *     public var left: TreeNode?
 *     public var right: TreeNode?
 *     public init(_ val: Int) {
 *         self.val = val
 *         self.left = nil
 *         self.right = nil
 *     }
 * }
 */

class Solution {
    func lowestCommonAncestor(_ root: TreeNode?, _ p: TreeNode?, _ q: TreeNode?) -> TreeNode? {
        guard let node = root else { return nil }

        if node === q || node === p { return node }

        let right = lowestCommonAncestor(node.right, p, q)
        let left = lowestCommonAncestor(node.left, p, q)

        if right != nil, left != nil { return node }
        return left ?? right
    }
}
