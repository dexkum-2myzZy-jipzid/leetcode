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
    func boundaryOfBinaryTree(_ root: TreeNode?) -> [Int] {
        // [root] + [left boundary] + [leaf] + [right boundary]
        guard let root = root else { return [] }
        var res: [Int] = [root.val]

        func isLeaf(_ node: TreeNode) -> Bool {
            return node.left == nil && node.right == nil
        }

        if isLeaf(root) { return res }

        // left boundary
        func getLeftBoundary(_ node: TreeNode?) {
            guard let node = node else { return }
            var cur: TreeNode? = node

            while let n = cur {
                if isLeaf(n) { break }
                res.append(n.val)
                cur = n.left ?? n.right
            }
        }

        func getRightBoundary(_ node: TreeNode?) {
            guard let node = node else { return }
            var cur: TreeNode? = node
            var ans: [Int] = []

            while let n = cur {
                if isLeaf(n) { break }
                ans.append(n.val)
                cur = n.right ?? n.left
            }

            res.append(contentsOf: ans.reversed())
        }

        func getLeaves(_ root: TreeNode?) {
            guard let root = root else { return }

            if isLeaf(root) { res.append(root.val) }
            getLeaves(root.left)
            getLeaves(root.right)
        }

        getLeftBoundary(root.left)
        getLeaves(root)
        getRightBoundary(root.right)

        return res
    }
}
