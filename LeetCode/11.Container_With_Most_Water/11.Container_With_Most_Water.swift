class Solution {
    func maxArea(_ height: [Int]) -> Int {
        // two pointer
        let n = height.count
        var l = 0, r = n - 1

        var res = 0
        while l < r {
            res = max(res, (r - l) * min(height[l], height[r]))

            if height[l] < height[r] {
                l += 1
            } else {
                r -= 1
            }
        }

        return res
    }
}
