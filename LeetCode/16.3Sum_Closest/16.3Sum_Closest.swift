class Solution {
    func threeSumClosest(_ nums: [Int], _ target: Int) -> Int {
        // sum(3 int) closest to target
        // [-4, -1, 1, 2]  a + b + c = target
        // a + b = target - c
        // two pointer to find (target-c), which is closest to (target-c)
        // if a + b = t, return target
        // if a + b < t: a += 1
        // if a + b > t: b -= 1

        var nums = nums.sorted()
        let n = nums.count
        var res = nums[0] + nums[1] + nums[2]

        for (i, num) in nums.enumerated() {
            if i > 0 && num == nums[i - 1] { continue }
            let t = target - num
            // find a, b, which closest to t
            var l = i + 1, r = n - 1
            while l < r {
                let sum2 = nums[l] + nums[r]
                if abs(res - target) > abs(sum2 - t) {
                    res = sum2 + num
                }
                if sum2 == t {
                    return target
                } else if sum2 < t {
                    l += 1
                } else {
                    r -= 1
                }
            }
        }

        return res
    }
}
