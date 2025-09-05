class Solution {
    func addStrings(_ num1: String, _ num2: String) -> String {
        let num1 = Array(num1), num2 = Array(num2)
        let m = num1.count, n = num2.count

        var i = m - 1, j = n - 1
        var carry = 0
        var res: [Character] = []

        while i >= 0 || j >= 0 || carry != 0 {
            var total = carry
            if i >= 0 {
                total += Int(String(num1[i]))!
                i -= 1
            }
            if j >= 0 {
                total += Int(String(num2[j]))!
                j -= 1
            }

            carry = total / 10
            res.append(Character(String(total % 10)))
        }

        return String(res.reversed())
    }
}

let s = Solution()
print(s.addStrings("456", "77"))
