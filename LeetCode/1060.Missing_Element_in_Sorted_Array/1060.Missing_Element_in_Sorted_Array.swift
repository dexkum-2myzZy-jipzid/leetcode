class Solution {
    func missingElement(_ nums: [Int], _ k: Int) -> Int {
        // compare missing num count, binary search
        let n = nums.count

        // [4, 7, 9, 10]
        // i = 2 nums[2] = 9, 9 - 4 - 2 = 3 (5, 6, 8)
        // how many num missing at index i
        func missing(_ i: Int) -> Int {
            return nums[i] - nums[0] - i
        }

        // last >= k
        var l = 0, r = n
        while l < r {
            let m = (l + r) / 2
            if missing(m) < k {
                l = m + 1
            } else {
                r = m
            }
        }

        return nums[l - 1] + k - missing(l - 1)
    }
}
