class Solution {
    func twoSum(_ nums: [Int], _ target: Int) -> [Int] {
        var dic :[Int:Int] = [:]
        for (i, num) in nums.enumerated(){
            if let idx = dic[target-num]{
                return [idx, i]
            }
            dic[num] = i
        }
        return []
    }
}

// test
let s = Solution()
let res = s.twoSum([2,7,11,15], 9)
print("res:\(res)")