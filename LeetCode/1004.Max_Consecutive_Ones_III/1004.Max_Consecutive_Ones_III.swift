class Solution {
    func longestOnes(_ nums: [Int], _ k: Int) -> Int {
        // max num of consecutive 1's if flip at most k 0's
        // sliding window, count flip num of 0's
        // if > k, shift left pointer to right
        // if < k, shift right pointer

        let n = nums.count
        guard n > k else { return n }

        var l = 0, cnt = 0
        var res = 0

        for (i, num) in nums.enumerated() {
            cnt = num == 0 ? cnt + 1 : cnt

            while cnt > k && l <= i {
                cnt = nums[l] == 0 ? cnt - 1 : cnt
                l += 1
            }

            res = max(res, i - l + 1)
        }

        return res
    }
}
