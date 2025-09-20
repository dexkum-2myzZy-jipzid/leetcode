class Solution {
    func searchRange(_ nums: [Int], _ target: Int) -> [Int] {
        let n = nums.count
        var l = 0, r = n

        while l < r {
            let mid = (l + r) >> 1
            if nums[mid] < target {
                l = mid + 1
            } else {
                r = mid
            }
        }

        var res: [Int] = []
        if l < n, nums[l] == target {
            res.append(l)
        } else {
            return [-1, -1]
        }

        l = 0
        r = n
        while l < r {
            let mid = (l + r) >> 1
            if nums[mid] > target {
                r = mid
            } else {
                l = mid + 1
            }
        }

        res.append(l - 1)

        return res
    }
}
