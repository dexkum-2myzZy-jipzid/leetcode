class Solution {
    func findMedianSortedArrays(_ nums1: [Int], _ nums2: [Int]) -> Double {
        // i, j
        // nums[i] < nums[j+1] && nums[j] < nums[i+1] && (i+j+2) == leftCnt

        // nums1.count <= num2.count
        let (a, b) = nums1.count <= nums2.count ? (nums1, nums2) : (nums2, nums1)
        let m = a.count, n = b.count
        let leftCnt = (m + n + 1) / 2

        var l = 0, r = m

        while l <= r {
            let i = (l + r) / 2
            let j = leftCnt - i

            let aLeft = i == 0 ? Int.min : a[i - 1]
            let aRight = i == m ? Int.max : a[i]
            let bLeft = j == 0 ? Int.min : b[j - 1]
            let bRight = j == n ? Int.max : b[j]

            if aLeft <= bRight && bLeft <= aRight {
                if (m + n) & 1 == 1 {
                    return Double(max(aLeft, bLeft))
                } else {
                    let leftMax = Double(max(aLeft, bLeft))
                    let rightMin = Double(min(aRight, bRight))
                    return (leftMax + rightMin) / 2.0
                }
            } else if aLeft > bRight {
                // shrink a left
                r = i - 1
            } else {
                l = i + 1
            }
        }

        return 0.0
    }
}
