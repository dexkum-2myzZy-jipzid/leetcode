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

// recursive
class Solution {
    func closestValue(_ root: TreeNode?, _ target: Double) -> Int {
        // righht val > root.val > left val
        // if node.val < target, dfs(node.right)
        // if node.val > target, dfs(node.left)

        var res = Int.max
        var minDiff = abs(Double(res) - target)

        func dfs(_ node: TreeNode?) {
            guard let node = node else {
                return
            }

            let diff = abs(target - Double(node.val))

            if diff < minDiff || (diff == minDiff && node.val < res) {
                res = node.val
                minDiff = diff
            }

            if Double(node.val) < target {
                dfs(node.right)
            } else if Double(node.val) > target {
                dfs(node.left)
            } else {
                return
            }
        }

        dfs(root)

        return res
    }
}

// while
class Solution {
    // 迭代解：O(h) 时间，O(1) 额外空间
    func closestValue(_ root: TreeNode?, _ target: Double) -> Int {
        guard var node = root else { return 0 } // 题目保证非空，防御性处理

        var best = node.val
        var bestDiff = abs(Double(best) - target)

        while true {
            let v = node.val
            let diff = abs(Double(v) - target)

            // 更接近就更新；平局时取更小值（可选的确定性 tie-break）
            if diff < bestDiff || (diff == bestDiff && v < best) {
                best = v
                bestDiff = diff
            }

            if target < Double(v) {
                if let left = node.left { node = left } else { break }
            } else if target > Double(v) {
                if let right = node.right { node = right } else { break }
            } else {
                return v // 完全相等，最优
            }
        }
        return best
    }
}
