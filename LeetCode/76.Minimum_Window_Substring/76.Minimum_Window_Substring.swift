class Solution {
    func minWindow(_ s: String, _ t: String) -> String {
        let sArr = Array(s), tArr = Array(t)
        guard sArr.count >= tArr.count else { return "" }

        var count: [Character: Int] = [:]
        for ch in tArr {
            count[ch, default: 0] += 1
        }
        var missing = count.count

        var (start, len) = (0, Int.max)
        var left = 0
        for (right, ch) in sArr.enumerated() {
            if let cnt = count[ch] {
                count[ch] = cnt - 1
                if count[ch] == 0 { missing -= 1 }
            }

            while missing == 0 {
                let lch = sArr[left]
                if let c = count[lch] {
                    if c >= 0 { break }
                    count[lch] = c + 1
                }
                left += 1
            }

            if missing == 0 {
                let curLen = right - left + 1
                if curLen < len { (start, len) = (left, curLen) }
            }
        }

        return len == Int.max ? "" : String(sArr[start ..< start + len])
    }
}
