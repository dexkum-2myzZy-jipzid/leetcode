class Solution {
    func alienOrder(_ words: [String]) -> String {
        // t -> f, w -> e, r -> t, e -> r
        // wertf, toplogical sort
        let n = words.count
        let chs = words.map { Array($0) }
        var indeg: [Character: Int] = [:]

        let keys = Set(words.joined())
        for k in keys {
            indeg[k] = 0
        }

        // build graph
        var graph: [Character: [Character]] = [:]
        for i in 1 ..< n {
            let pre = chs[i - 1], cur = chs[i]
            var diff = false
            for (a, b) in zip(pre, cur) {
                if a != b {
                    graph[a, default: []].append(b)
                    indeg[b, default: 0] += 1
                    diff = true
                    break
                }
            }
            // no diff in word, pre word is longer than current
            // it's impossible
            if !diff && (pre.count > cur.count) {
                return ""
            }
        }

        // print(indeg)
        // print(graph)

        // toplogical sort kahn algo
        // queue (node, path)
        var q: [Character] = []
        var head = 0
        for (k, v) in indeg where v == 0 {
            q.append(k)
        }

        var res: [Character] = []
        while head < q.count {
            let node = q[head]
            head += 1
            res.append(node)

            for nei in graph[node, default: []] {
                indeg[nei] = indeg[nei]! - 1
                if indeg[nei] == 0 {
                    q.append(nei)
                }
            }
        }

        return res.count == indeg.count ? String(res) : ""
    }
}
