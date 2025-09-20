class Solution {
    func isPalindrome(_ s: String) -> Bool {
        let chars = Array(s)
        var left = 0
        var right = chars.count - 1

        while left < right {
            while left < right && !chars[left].isLetter && !chars[left].isNumber {
                left += 1
            }
            while left < right && !chars[right].isLetter && !chars[right].isNumber {
                right -= 1
            }

            if chars[left].lowercased() != chars[right].lowercased() {
                return false
            }

            left += 1
            right -= 1
        }

        return true
    }
}

let solution = Solution()
let s = "A man, a plan, a canal: Panama"
print(solution.isPalindrome(s))
