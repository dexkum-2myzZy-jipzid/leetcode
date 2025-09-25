class Solution {
    func ladderLength(_ beginWord: String, _ endWord: String, _ wordList: [String]) -> Int {
        // shortest transformation seq, bfs
        // adjacent pair diff 1 letter
        var wordSet = Set(wordList)
        guard wordSet.contains(endWord) else { return 0 }

        wordSet.insert(beginWord)
        let wordArr = Array(wordSet)
        // 26 * 10 * 5000
        // hit -> *it, h*t, hi*
        var graph: [String: [String]] = [:]
        for word in wordSet {
            var wordArr = Array(word)
            for i in 0 ..< wordArr.count {
                let old = wordArr[i]
                wordArr[i] = "*"
                let key = String(wordArr)
                graph[key, default: []].append(word)
                wordArr[i] = old
            }
        }

        var q: [(String, Int)] = [(beginWord, 1)]
        var head = 0
        var seen: Set<String> = [beginWord]

        while head < q.count {
            let (cur, step) = q[head]
            head += 1

            if cur == endWord { return step }

            var curArr = Array(cur)
            for i in 0 ..< curArr.count {
                let old = curArr[i]
                curArr[i] = "*"
                let key = String(curArr)
                for nei in graph[key, default: []] {
                    if !seen.contains(nei) {
                        seen.insert(nei)
                        q.append((nei, step + 1))
                    }
                }
                curArr[i] = old
            }
        }

        return 0
    }
}
