class Solution {
    func isValid(_ s: String) -> Bool {
        let brackets: [Character: Character] = [")": "(", "]": "[", "}": "{"]
        var stack: [Character] = []

        for ch in s {
            if let need = brackets[ch] {
                guard let top = stack.popLast(), top == need else {
                    return false
                }
            } else {
                stack.append(ch)
            }
        }

        return stack.isEmpty
    }
}
