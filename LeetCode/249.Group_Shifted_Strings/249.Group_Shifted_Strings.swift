class Solution {
    func groupStrings(_ strings: [String]) -> [[String]] {
        // right shift: a->b
        // left shift: a -> z
        // abc -> 123

        var buckets: [String: [String]] = [:]
        for s in strings {
            let key = getKey(s)
            // print(key)
            buckets[key, default: []].append(s)
        }

        var res: [[String]] = []
        for v in buckets.values {
            res.append(v)
        }

        return res
    }

    func getKey(_ s: String) -> String {
        let bytes = Array(s.utf8).map { Int($0) }
        let n = bytes.count
        guard n > 1 else { return "#" }

        var parts: [String] = []
        for i in 1 ..< n {
            let diff = ((bytes[i] - bytes[i - 1]) + 26) % 26
            parts.append(String(diff))
        }

        return parts.joined(separator: "#")
    }
}
