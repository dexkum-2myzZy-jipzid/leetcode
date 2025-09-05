class Solution {
    func validPalindrome(_ s: String) -> Bool {
        // delete at most one character
        let chars = Array(s)
        let n = chars.count
        var left = 0
        var right = n - 1

        func isPalindrome(_ l: Int, _ r: Int) -> Bool {
            var l = l, r = r
            while l < r {
                if chars[l] != chars[r] {
                    return false
                }
                l += 1
                r -= 1
            }
            return true
        }

        while left < right {
            if chars[left] == chars[right] {
                left += 1
                right -= 1
            } else {
                return isPalindrome(left + 1, right) || isPalindrome(left, right - 1)
            }
        }

        return true
    }
}
