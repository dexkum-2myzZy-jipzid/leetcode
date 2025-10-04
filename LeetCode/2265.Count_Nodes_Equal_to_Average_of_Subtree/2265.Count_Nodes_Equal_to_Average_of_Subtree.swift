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
    func averageOfSubtree(_ root: TreeNode?) -> Int {
        // the num of nodes, val == average of substree
        var res = 0

        // sum of tree, the num of node
        func dfs(_ node: TreeNode?) -> (Int, Int) {
            guard let node = node else { return (0, 0) }

            let (lSum, lCnt) = dfs(node.left)
            let (rSum, rCnt) = dfs(node.right)

            let sum = lSum + rSum + node.val
            let cnt = lCnt + rCnt + 1

            if sum / cnt == node.val {
                res += 1
            }

            return (sum, cnt)
        }

        dfs(root)

        return res
    }
}
