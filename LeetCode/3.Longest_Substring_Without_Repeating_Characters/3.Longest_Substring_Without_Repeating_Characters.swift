// dictionary hold previous count
class Solution {
    func lengthOfLongestSubstring(_ s: String) -> Int {
        var chs = Array(s.utf8)
        var counter: [UInt8: Int] = [:]
        var l = 0, res = 0

        for (i, ch) in chs.enumerated() {
            counter[ch, default: 0] += 1

            while counter[ch, default: 0] > 1 {
                counter[chs[l], default: 0] -= 1
                l += 1
            }

            res = max(res, i - l + 1)
        }

        return res
    }
}

// dictionary hold previous position
class Solution {
    func lengthOfLongestSubstring(_ s: String) -> Int {
        var chs = Array(s.utf8)
        // value: previous position
        var prevPos: [UInt8: Int] = [:]
        var l = 0, res = 0

        for (i, ch) in chs.enumerated() {
            while let prev = prevPos[ch], prev >= l {
                l = prev + 1
            }

            prevPos[ch] = i
            res = max(res, i - l + 1)
        }

        return res
    }
}
