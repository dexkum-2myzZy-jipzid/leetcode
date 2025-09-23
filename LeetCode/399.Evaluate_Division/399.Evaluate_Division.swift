// dfs
class Solution {
    func calcEquation(_ equations: [[String]], _ values: [Double], _ queries: [[String]]) -> [Double] {
        // a:[(b, 2.0)] b:[(a, 1/2.0), (c, 3.0)], c:[(b, 1/3.0)]

        // build graph
        var graph: [String: [(String, Double)]] = [:]
        var nodes: Set<String> = []
        for (i, e) in equations.enumerated() {
            let a = e[0], b = e[1], val = values[i]
            graph[a, default: []].append((b, val))
            graph[b, default: []].append((a, 1.0 / val))
            nodes.insert(a)
            nodes.insert(b)
        }

        var seen = Set<String>()

        func dfs(_ s: String, _ e: String, _ cur: Double) -> Double {
            seen.insert(s)

            if !nodes.contains(s) || !nodes.contains(e) { return -1.0 }
            if s == e { return cur }

            guard let neis = graph[s] else { return -1.0 }
            for nei in neis {
                let (v, val) = nei
                if seen.contains(v) {
                    continue
                }
                if v == e {
                    return cur * val
                } else {
                    let res = dfs(v, e, cur * val)
                    if res == -1.0 {
                        continue
                    } else {
                        return res
                    }
                }
            }

            return -1.0
        }

        var res: [Double] = []
        for q in queries {
            let a = q[0], b = q[1]
            seen.removeAll()
            res.append(dfs(a, b, 1.0))
        }

        return res
    }
}

// bfs
class Solution {
    func calcEquation(_ equations: [[String]], _ values: [Double], _ queries: [[String]]) -> [Double] {
        // a:[(b, 2.0)] b:[(a, 1/2.0), (c, 3.0)], c:[(b, 1/3.0)]

        // build graph
        var graph: [String: [(String, Double)]] = [:]
        var nodes: Set<String> = []
        for (i, e) in equations.enumerated() {
            let a = e[0], b = e[1], val = values[i]
            graph[a, default: []].append((b, val))
            graph[b, default: []].append((a, 1.0 / val))
            nodes.insert(a)
            nodes.insert(b)
        }

        var seen = Set<String>()

        func bfs(_ s: String, _ e: String) -> Double {
            if !nodes.contains(s) || !nodes.contains(e) { return -1.0 }
            if s == e { return 1.0 }

            var q: [(String, Double)] = [(s, 1.0)]
            var head = 0
            var seen: Set<String> = [s]

            while head < q.count {
                let (cur, curVal) = q[head]
                head += 1

                if cur == e {
                    return curVal
                }

                for (nei, weight) in graph[cur, default: []] {
                    if !seen.contains(nei) {
                        let neiVal = weight * curVal
                        seen.insert(nei)
                        q.append((nei, neiVal))
                    }
                }
            }

            return -1.0
        }

        var res: [Double] = []
        for q in queries {
            let a = q[0], b = q[1]
            res.append(bfs(a, b))
        }

        return res
    }
}
