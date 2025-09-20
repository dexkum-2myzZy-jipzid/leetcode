class Solution {
    func containsNearbyDuplicate(_ nums: [Int], _ k: Int) -> Bool {
        var idxMap: [Int: Int] = [:]

        for (i, num) in nums.enumerated() {
            if let j = idxMap[num] {
                if i - j <= k {
                    return true
                }
            }
            idxMap[num] = i
        }

        return false
    }
}
