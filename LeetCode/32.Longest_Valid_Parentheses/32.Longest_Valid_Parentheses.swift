class Solution {
    func longestValidParentheses(_ s: String) -> Int {
        var res = 0
        var stack: [Int] = [-1] // hold index of left parenthesis

        for (i, ch) in Array(s).enumerated() {
            if ch == "(" {
                stack.append(i)
            } else if ch == ")" {
                _ = stack.popLast()
                if stack.isEmpty {
                    stack.append(i)
                } else {
                    res = max(res, i - stack.last!)
                }
            }
        }

        return res
    }
}

class Solution {
    func longestValidParentheses(_ s: String) -> Int {
        let chs = Array(s)
        let n = chs.count

        var dp = Array(repeating: 0, count: n)
        var res = 0

        for (i, ch) in chs.enumerated() {
            guard i > 0, ch == ")" else { continue }

            // ()
            if chs[i - 1] == "(" {
                dp[i] = (i - 2 >= 0 ? dp[i - 2] : 0) + 2
            } else {
                // (())
                let j = i - dp[i - 1] - 1
                if j >= 0 && chs[j] == "(" {
                    dp[i] = dp[i - 1] + 2 + (j >= 1 ? dp[j - 1] : 0)
                }
            }

            res = max(res, dp[i])
        }

        return res
    }
}
