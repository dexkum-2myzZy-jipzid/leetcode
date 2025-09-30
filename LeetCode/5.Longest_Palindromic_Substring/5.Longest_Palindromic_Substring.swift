class Solution {
    func longestPalindrome(_ s: String) -> String {
        let chs = Array(s)
        let n = chs.count

        var (start, len) = (0, 1)

        func helper(_ l: Int, _ r: Int) {
            var l = l, r = r

            while l >= 0 && r < n && chs[l] == chs[r] {
                let curLen = r - l + 1
                if curLen > len {
                    (start, len) = (l, curLen)
                }
                l -= 1
                r += 1
            }
        }

        for i in 0 ..< n {
            helper(i, i)
            if i > 0 {
                helper(i - 1, i)
            }
        }

        return String(chs[start ..< start + len])
    }
}

// DP
class Solution {
    func longestPalindrome(_ s: String) -> String {
        let chs = Array(s)
        let n = chs.count

        var dp = Array(repeating: Array(repeating: false, count: n), count: n)

        var (start, len) = (0, 1)

        // init dp
        for i in 0 ..< n {
            dp[i][i] = true
            if i > 0 && chs[i - 1] == chs[i] {
                dp[i - 1][i] = true
                if len < 2 {
                    (start, len) = (i - 1, 2)
                }
            }
        }

        if n >= 3 {
            for l in 3 ... n {
                for left in 0 ..< n {
                    let right = left + l - 1
                    if right >= n { break }

                    dp[left][right] = dp[left + 1][right - 1] && (chs[left] == chs[right])
                    if dp[left][right] && l > len {
                        (start, len) = (left, l)
                    }
                }
            }
        }

        return String(chs[start ..< start + len])
    }
}
