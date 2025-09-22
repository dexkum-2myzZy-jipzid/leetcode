class Solution {
    func nextPermutation(_ nums: inout [Int]) {
        // scan backward to find index i where nums[i] < nums[i+1]
        let n = nums.count
        var l = -1
        for i in stride(from: n - 2, through: 0, by: -1) {
            if nums[i] < nums[i + 1] {
                l = i + 1
                break
            }
        }

        // find element which is smallest bigger than nums[i]
        // scan backword again
        if l == -1 {
            l = 0
        } else {
            var j = n - 1
            while j >= 0, nums[j] <= nums[l - 1] {
                j -= 1
            }
            nums.swapAt(j, l - 1)
        }

        // sort right part nums[i+1:]
        var r = n - 1
        while l < r {
            nums.swapAt(l, r)
            l += 1
            r -= 1
        }
    }
}
