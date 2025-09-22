class Solution {
    func canFinish(_ numCourses: Int, _ prerequisites: [[Int]]) -> Bool {
        // [ai, bi] bi -> ai
        // Dijstra
        var indegree = Array(repeating: 0, count: numCourses)
        var graph: [Int: [Int]] = [:]

        for pre in prerequisites {
            let (a, b) = (pre[0], pre[1])
            graph[b, default: []].append(a)
            indegree[a] += 1
        }

        var q: [Int] = []
        for (i, v) in indegree.enumerated() {
            if v == 0 {
                q.append(i)
            }
        }

        var head = 0

        while head < q.count {
            let i = q[head]
            head += 1
            if let neis = graph[i] {
                for nei in neis {
                    indegree[nei] -= 1
                    if indegree[nei] == 0 {
                        q.append(nei)
                    }
                }
            }
        }

        return indegree.allSatisfy { $0 == 0 }
    }
}
