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
