class Solution {
    func maxFrequencyElements(_ nums: [Int]) -> Int {
        var buckets = Array(repeating: 0, count: 101)

        var maxFreq = 0
        for num in nums {
            buckets[num] += 1
            maxFreq = max(maxFreq, buckets[num])
        }

        return buckets.reduce(0) { pre, cur in
            pre + (cur == maxFreq ? cur : 0)
        }
    }
}
