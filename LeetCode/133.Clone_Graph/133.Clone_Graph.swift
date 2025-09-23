/**
 * Definition for a Node.
 * public class Node {
 *     public var val: Int
 *     public var neighbors: [Node?]
 *     public init(_ val: Int) {
 *         self.val = val
 *         self.neighbors = []
 *     }
 * }
 */

class Solution {
    func cloneGraph(_ node: Node?) -> Node? {
        // dic: val: Copy Node
        guard let node = node else { return nil }

        var dic: [Int: Node] = [:]

        func dfs(_ node: Node?) -> Node? {
            guard let node = node else { return nil }

            if let copy = dic[node.val] {
                return copy
            }

            let copy = Node(node.val)
            dic[node.val] = copy
            for nei in node.neighbors {
                copy.neighbors.append(dfs(nei))
            }
            return copy
        }

        return dfs(node)
    }
}
