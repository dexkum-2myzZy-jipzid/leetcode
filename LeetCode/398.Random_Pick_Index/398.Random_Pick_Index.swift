
class Solution {
    var dic: [Int: [Int]] = [:]

    init(_ nums: [Int]) {
        for (i, num) in nums.enumerated() {
            dic[num, default: []].append(i)
        }
    }

    func pick(_ target: Int) -> Int {
        if let arr = dic[target] {
            let i = Int.random(in: 0 ..< arr.count)
            return arr[i]
        }
        return -1
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * let obj = Solution(nums)
 * let ret_1: Int = obj.pick(target)
 */
