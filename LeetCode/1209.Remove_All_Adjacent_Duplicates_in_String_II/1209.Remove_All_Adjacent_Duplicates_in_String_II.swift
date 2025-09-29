class Solution {
    func removeDuplicates(_ s: String, _ k: Int) -> String {
        // ("a", count)
        // stack
        var stack: [(Character, Int)] = []

        for ch in s {
            if var top = stack.last, top.0 == ch {
                top.1 += 1
                stack[stack.count - 1] = top
                if top.1 == k {
                    stack.removeLast()
                }
            } else {
                stack.append((ch, 1))
            }
        }

        return stack.reduce("") { acc, e in
            acc + String(repeating: e.0, count: e.1)
        }
    }
}
