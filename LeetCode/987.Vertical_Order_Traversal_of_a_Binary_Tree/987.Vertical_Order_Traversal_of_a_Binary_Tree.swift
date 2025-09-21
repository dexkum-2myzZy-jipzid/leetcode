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
    func verticalTraversal(_ root: TreeNode?) -> [[Int]] {
        var nodes: [(Int, Int, Int)] = []

        func dfs(_ node: TreeNode?, _ row: Int, _ col: Int) {
            guard let node = node else { return }

            nodes.append((node.val, row, col))
            dfs(node.left, row + 1, col - 1)
            dfs(node.right, row + 1, col + 1)
        }

        dfs(root, 0, 0)

        nodes.sort { a, b in
            (a.2, a.1, a.0) < (b.2, b.1, b.0)
        }

        // print(nodes)

        let n = nodes.count
        var res: [[Int]] = []
        var prevCol: Int? = nil
        for (val, row, col) in nodes {
            if prevCol == nil || prevCol != col {
                res.append([val])
                prevCol = col
            } else {
                res[res.count - 1].append(val)
            }
        }

        return res
    }
}

// using dict to group col
class Solution {
    func verticalTraversal(_ root: TreeNode?) -> [[Int]] {
        var groups: [Int: [(Int, Int)]] = [:]

        func dfs(_ node: TreeNode?, _ row: Int, _ col: Int) {
            guard let node = node else { return }

            groups[col, default: []].append((node.val, row))
            dfs(node.left, row + 1, col - 1)
            dfs(node.right, row + 1, col + 1)
        }

        dfs(root, 0, 0)

        // print(groups)

        let n = groups.count
        var res: [[Int]] = []
        for (k, v) in groups.sorted(by: { $0.key < $1.key }) {
            let sort = v.sorted { ($0.1, $0.0) < ($1.1, $1.0) }
            res.append(sort.map { $0.0 })
        }

        return res
    }
}
