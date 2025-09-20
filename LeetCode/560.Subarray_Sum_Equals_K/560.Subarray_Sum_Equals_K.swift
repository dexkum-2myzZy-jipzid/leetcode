class Solution {
    func subarraySum(_ nums: [Int], _ k: Int) -> Int {
        var last = 0
        var dic = [0: 1]

        var res = 0
        for num in nums {
            last += num
            if let cnt = dic[last - k] {
                res += cnt
            }
            dic[last, default: 0] += 1
        }

        return res
    }
}
