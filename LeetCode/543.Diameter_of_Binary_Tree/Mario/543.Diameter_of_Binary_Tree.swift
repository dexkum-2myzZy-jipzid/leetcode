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
    func diameterOfBinaryTree(_ root: TreeNode?) -> Int {
        var diameter = 0
        
        func helper(_ node: TreeNode?) -> Int {
            guard let node = node else {
                return 0
            }
            
            let left = helper(node.left)
            let right = helper(node.right)

            diameter = max(diameter, left + right)

            return max(left, right) + 1
        }

        helper(root)

        return diameter
    }
}