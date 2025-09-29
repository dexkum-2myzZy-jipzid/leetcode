class Solution {
    func minAddToMakeValid(_ s: String) -> Int {
        // stack, push "(" into stack
        // if meet ")", pop stack, if stack is empty, we will use closed to count
        var stack: [Character] = []
        var closed = 0

        for ch in s {
            if ch == "(" {
                stack.append(ch)
            } else {
                if !stack.isEmpty {
                    stack.removeLast()
                } else {
                    closed += 1
                }
            }
        }

        return stack.count + closed
    }
}
