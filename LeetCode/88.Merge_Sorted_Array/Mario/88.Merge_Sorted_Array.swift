class Solution {
    func merge(_ nums1: inout [Int], _ m: Int, _ nums2: [Int], _ n: Int) {
        // backforwad traversal this nums1
        // put largest num first, then decrease
        var j = m - 1
        var k = n - 1
        for i in (0 ..< (m + n)).reversed() {
            // j & k > 0
            var tmp = -1
            if j >= 0, k >= 0 {
                if nums1[j] >= nums2[k] {
                    nums1[i] = nums1[j]
                    j -= 1
                } else {
                    nums1[i] = nums2[k]
                    k -= 1
                }
            } else if j >= 0 {
                nums1[i] = nums1[j]
                j -= 1
            } else {
                nums1[i] = nums2[k]
                k -= 1
            }
        }
    }
}
