class Solution {
    func countSubstrings(_ s: String) -> Int {
        // expand from center
        let arr = Array(s)
        let n = arr.count

        func paliCountFromCenter(_ l: Int, _ r: Int) -> Int {
            var l = l, r = r
            var cnt = 0
            while l >= 0 && r < n && arr[l] == arr[r] {
                cnt += 1
                l -= 1
                r += 1
            }

            return cnt
        }

        var res = 0
        for i in 0 ..< n {
            res += paliCountFromCenter(i, i)
            if i > 0 {
                res += paliCountFromCenter(i - 1, i)
            }
        }

        return res
    }
}

// String.index
class Solution2 {
    func countSubstrings(_ s: String) -> Int {
        let n: Int = s.count
        guard n > 0 else { return 0 }

        var res = 0

        func paliCountFromCenter(_ l: String.Index, _ r: String.Index) -> Int {
            var cnt = 0
            var l: String.Index = l, r: String.Index = r

            while l >= s.startIndex && r < s.endIndex && s[l] == s[r] {
                cnt += 1

                if l == s.startIndex || r == s.index(before: s.endIndex) {
                    break
                }

                l = s.index(before: l)
                r = s.index(after: r)
            }
            return cnt
        }

        var i: String.Index = s.startIndex
        while i < s.endIndex {
            res += paliCountFromCenter(i, i)

            if i != s.startIndex {
                let prev: String.Index = s.index(before: i)
                res += paliCountFromCenter(prev, i)
            }

            i = s.index(after: i)
        }

        return res
    }
}
