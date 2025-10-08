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

extension TreeNode: Hashable {
    public static func == (_ lhs: TreeNode, _ rhs: TreeNode) -> Bool {
        lhs.val == rhs.val
    }

    public func hash(into hasher: inout Hasher) {
        hasher.combine(val)
    }
}

class Solution {
    func distanceK(_ root: TreeNode?, _ target: TreeNode?, _ k: Int) -> [Int] {
        // BFS -> build graph
        guard let root = root, let target = target else { return [] }

        var q: [TreeNode] = [root]
        var head = 0
        var graph: [TreeNode: [TreeNode]] = [:]

        while head < q.count {
            let node = q[head]
            head += 1

            if let left = node.left {
                graph[node, default: []].append(left)
                graph[left, default: []].append(node)
                q.append(left)
            }

            if let right = node.right {
                graph[node, default: []].append(right)
                graph[right, default: []].append(node)
                q.append(right)
            }
        }

        guard k > 0 else { return [target.val] }

        q = [target]
        head = 0
        var seen = Set<Int>()
        seen.insert(target.val)
        var step = 0
        var res: [Int] = []

        while step < k {
            let size = q.count - head
            step += 1

            for _ in 0 ..< size {
                let cur = q[head]
                head += 1

                for nei in graph[cur, default: []] {
                    if seen.contains(nei.val) { continue }
                    seen.insert(nei.val)

                    if step == k { res.append(nei.val) }
                    q.append(nei)
                }
            }
        }

        return res
    }
}

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
    func distanceK(_ root: TreeNode?, _ target: TreeNode?, _ k: Int) -> [Int] {
        // BFS -> build parent
        guard let root = root, let target = target else { return [] }

        var q: [TreeNode] = [root]
        var head = 0
        var parent: [ObjectIdentifier: TreeNode] = [:]

        while head < q.count {
            let node = q[head]
            head += 1

            if let left = node.left {
                parent[ObjectIdentifier(left)] = node
                q.append(left)
            }

            if let right = node.right {
                parent[ObjectIdentifier(right)] = node
                q.append(right)
            }
        }

        guard k > 0 else { return [target.val] }

        q = [target]
        head = 0
        var seen = Set<Int>()
        seen.insert(target.val)
        var step = 0
        var res: [Int] = []

        while step < k {
            let size = q.count - head
            step += 1

            for _ in 0 ..< size {
                let cur = q[head]
                head += 1

                let neis = [cur.left, cur.right, parent[ObjectIdentifier(cur)]].compactMap { $0 }

                for nei in neis {
                    if seen.contains(nei.val) { continue }
                    seen.insert(nei.val)

                    if step == k { res.append(nei.val) }
                    q.append(nei)
                }
            }
        }

        return res
    }
}
