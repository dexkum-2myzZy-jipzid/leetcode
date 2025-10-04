class Solution {
    func maxSubArray(_ nums: [Int]) -> Int {
        var res = Int.min
        var sub = 0

        for num in nums {
            sub += num
            res = max(res, sub)
            if sub < 0 {
                sub = 0
            }
        }

        return res
    }
}

class Solution {
    /// 返回最大连续子数组和
    func maxSubArray(_ nums: [Int]) -> Int {
        // 题目保证至少一个元素；若要健壮化可额外判断空数组
        var cur = nums[0] // 以当前索引结尾的最大和
        var ans = nums[0] // 全局最大和

        for i in 1 ..< nums.count {
            // 若 cur 为负，会拖累后续，直接从 nums[i] 重新开始
            cur = max(nums[i], cur + nums[i])
            ans = max(ans, cur)
        }
        return ans
    }
}
