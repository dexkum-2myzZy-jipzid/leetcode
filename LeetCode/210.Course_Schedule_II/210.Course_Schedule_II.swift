class Solution {
    func findOrder(_ numCourses: Int, _ prerequisites: [[Int]]) -> [Int] {
        // [0, numCourses-1]
        // [ai, bi] => bi -> ai
        // Dijstra

        var indeg: [Int] = Array(repeating: 0, count: numCourses)
        var graph: [Int: [Int]] = [:]

        for pre in prerequisites {
            let (a, b) = (pre[0], pre[1])
            graph[b, default: []].append(a)
            indeg[a] += 1
        }

        var res: [Int] = []
        var head = 0
        for (i, v) in indeg.enumerated() {
            if v == 0 {
                res.append(i)
            }
        }

        while head < res.count {
            let v = res[head]
            head += 1
            for nei in graph[v, default: []] {
                indeg[nei] -= 1
                if indeg[nei] == 0 {
                    res.append(nei)
                }
            }
        }

        return numCourses > res.count ? [] : res
    }
}
