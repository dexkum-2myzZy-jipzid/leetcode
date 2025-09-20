class Solution {
    func customSortString(_ order: String, _ s: String) -> String {
        // lowercase
        var freq: [Character: Int] = [:]
        for ch in s {
            freq[ch, default: 0] += 1
        }

        var res = ""
        for ch in order {
            if let f = freq[ch] {
                res += String(repeating: String(ch), count: f)
                freq[ch] = nil
            }
        }

        for (ch, f) in freq {
            res += String(repeating: String(ch), count: f)
        }

        return res
    }
}

class Solution {
    func customSortString(_ order: String, _ s: String) -> String {
        var rank: [Character: Int] = [:]
        for (i, ch) in order.enumerated() {
            rank[ch] = i
        }

        let n = s.count
        var res = Array(s)
        res.sort { a, b -> Bool in
            let ra = rank[a] ?? n
            let rb = rank[b] ?? n
            return ra < rb
        }

        return String(res)
    }
}
