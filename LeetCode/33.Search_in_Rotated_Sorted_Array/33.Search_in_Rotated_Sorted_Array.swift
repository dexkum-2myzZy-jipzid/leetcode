class Solution {
    func search(_ nums: [Int], _ target: Int) -> Int {
        let n = nums.count
        var l = 0, r = n
        // find pivot
        while l < r {
            let m = (l + r) / 2
            if nums[m] > nums[n - 1] {
                l = m + 1
            } else {
                r = m
            }
        }

        func binarySearch(_ l: Int, _ r: Int) -> Int {
            guard l <= r else { return -1 }

            var l = l, r = r
            while l < r {
                let m = (l + r) / 2
                if nums[m] == target {
                    return m
                } else if nums[m] < target {
                    l = m + 1
                } else {
                    r = m
                }
            }
            return -1
        }

        // [0..l-1] / [ l, n-1]
        if target > nums[n - 1] {
            return binarySearch(0, l)
        } else {
            return binarySearch(l, n)
        }

        return -1
    }
}
