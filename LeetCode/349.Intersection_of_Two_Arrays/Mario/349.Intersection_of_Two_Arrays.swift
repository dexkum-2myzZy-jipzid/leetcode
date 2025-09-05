class Solution {
    func intersection(_ nums1: [Int], _ nums2: [Int]) -> [Int] {
        var nums1 = Set(nums1), nums2 = Set(nums2)
        return Array(nums1.intersection(nums2))
    }
}

class Solution {
    func intersection(_ nums1: [Int], _ nums2: [Int]) -> [Int] {
        var nums1 = Set(nums1), nums2 = Set(nums2)
        if nums1.count > nums2.count {
            (nums1, nums2) = (nums2, nums1)
        }

        var res: [Int] = []
        for num in nums1 {
            if nums2.contains(num) {
                res.append(num)
            }
        }

        return res
    }
}
