class Solution {
    func minRemoveToMakeValid(_ s: String) -> String {
        // stack
        // if (, push it into stack
        // if ), if stack has (, pop
        var chars = Array(s)
        var stack: [Int] = []

        for (i, ch) in chars.enumerated() {
            if ch == "(" {
                stack.append(i)
            } else if ch == ")" {
                if !stack.isEmpty {
                    stack.removeLast()
                } else {
                    chars[i] = " "
                }
            }
        }

        for index in stack {
            chars[index] = " "
        }

        return String(chars).filter { $0 != " " }
    }
}
