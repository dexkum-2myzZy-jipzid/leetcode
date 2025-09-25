class Solution {
    func minMutation(_ startGene: String, _ endGene: String, _ bank: [String]) -> Int {
        // startGene -> endGene, if not return -1
        // a -> b  one mutation
        // bfs
        guard bank.contains(endGene) else { return -1 }

        var graph: [String: [String]] = [:]
        var bank = [startGene] + bank
        let n = bank.count

        func checkOneMut(_ a: String, _ b: String) -> Bool {
            guard a.count == b.count else { return false }

            var count = 0
            for i in a.indices {
                if a[i] != b[i] {
                    count += 1
                }
            }
            return count == 1
        }

        for i in 0 ..< n {
            let cur = bank[i]
            for j in 0 ..< i {
                let other = bank[j]
                if checkOneMut(cur, other) {
                    graph[cur, default: []].append(other)
                    graph[other, default: []].append(cur)
                }
            }
        }

        var q: [(String, Int)] = [(startGene, 0)]
        var head = 0
        var seen: Set<String> = [startGene]

        while head < q.count {
            let (s, step) = q[head]
            head += 1

            if s == endGene { return step }
            for nei in graph[s, default: []] {
                if !seen.contains(nei) {
                    seen.insert(nei)
                    q.append((nei, step + 1))
                }
            }
        }

        return -1
    }
}
