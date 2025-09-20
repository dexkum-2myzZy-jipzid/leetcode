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
    func verticalOrder(_ root: TreeNode?) -> [[Int]] {
        var arr: [(Int, Int, Int)] = []

        func dfs(_ node: TreeNode?, _ col: Int, _ row: Int) {
            guard let node = node else { return }

            arr.append((col, row, node.val))

            dfs(node.left, col - 1, row + 1)
            dfs(node.right, col + 1, row + 1)
        }

        dfs(root, 0, 0)

        arr.sort { ($0.0, $0.1) < ($1.0, $1.1) }

        var res: [[Int]] = []
        var preCol = Int.min
        for (c, r, v) in arr {
            if c != preCol {
                res.append([])
                preCol = c
            }
            res[res.count - 1].append(v)
        }

        return res
    }
}
