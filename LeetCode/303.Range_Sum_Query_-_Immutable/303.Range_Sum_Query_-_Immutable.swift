
class NumArray {
    var prefixSum = [0]

    init(_ nums: [Int]) {
        for num in nums {
            if let last = prefixSum.last {
                prefixSum.append(num + last)
            }
        }
    }

    func sumRange(_ left: Int, _ right: Int) -> Int {
        return prefixSum[right + 1] - prefixSum[left]
    }
}

/**
 * Your NumArray object will be instantiated and called as such:
 * let obj = NumArray(nums)
 * let ret_1: Int = obj.sumRange(left, right)
 */
