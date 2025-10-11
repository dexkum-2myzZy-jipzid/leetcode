class Solution {
    func minTime(_: Int, _ edges: [[Int]], _ hasApple: [Bool]) -> Int {
        // dfs, if this return no apple, so not include this path
        var graph: [Int: [Int]] = [:]
        for e in edges {
            let (a, b) = (e[0], e[1])
            graph[a, default: []].append(b)
            graph[b, default: []].append(a)
        }

        var seen = Set<Int>()

        // return hasApple, length
        func dfs(_ i: Int) -> Int {
            guard let neis = graph[i] else { return 0 }

            var path = 0
            for nei in neis {
                if !seen.contains(nei) {
                    seen.insert(nei)
                    let dis = dfs(nei)
                    if dis > 0 || hasApple[nei] {
                        path += 2 + dis
                    }
                }
            }
            return path
        }

        seen.insert(0)
        return dfs(0)
    }
}
