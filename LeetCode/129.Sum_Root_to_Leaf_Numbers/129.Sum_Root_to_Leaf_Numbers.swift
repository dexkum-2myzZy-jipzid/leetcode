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
    func sumNumbers(_ root: TreeNode?) -> Int {
        // [0, 9]
        func dfs(_ node: TreeNode?, _ parent: Int) -> Int {
            guard let node = node else { return 0 }

            let val = parent * 10 + node.val
            if node.left == nil && node.right == nil {
                return val
            }
            return dfs(node.left, val) + dfs(node.right, val)
        }

        return dfs(root, 0)
    }
}
