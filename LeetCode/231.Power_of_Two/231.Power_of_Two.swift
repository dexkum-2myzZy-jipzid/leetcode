class Solution {
    func isPowerOfTwo(_ n: Int) -> Bool {
        // binary search, left = 0, right 32
        // if 2**mid > n, right = mid
        // if 2**mid < n, left = mid + 1
        // if ==: true
        if n < 1 {
            return false
        }

        var l = 0, r = 32
        while l < r {
            let mid = (l + r) >> 1
            let cur = 1 << mid
            if cur == n {
                return true
            } else if cur < n {
                l = mid + 1
            } else {
                r = mid
            }
        }

        return false
    }
}
