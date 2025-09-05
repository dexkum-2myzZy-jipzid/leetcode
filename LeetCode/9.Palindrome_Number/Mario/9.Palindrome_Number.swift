class Solution {
    func isPalindrome(_ x: Int) -> Bool {
        if x == 0 { return true }
        if x < 0 || x % 10 == 0 {
            return false
        }
        var left = x, right = 0
        while left > right {
            right = right * 10 + left % 10
            left /= 10
        }

        return left == right || left == right / 10
    }
}
