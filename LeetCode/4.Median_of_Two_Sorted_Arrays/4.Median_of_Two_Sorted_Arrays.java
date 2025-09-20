class Solution {

    private int p1 = 0, p2 = 0;

    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int n = nums1.length + nums2.length;
        // odd
        if (n % 2 == 1) {
            for (int i = 0; i < n / 2; i++) {
                helper(nums1, nums2);
            }
            return helper(nums1, nums2);
        } else { // even
            for (int i = 0; i < n / 2 - 1; i++) {
                helper(nums1, nums2);
            }
            return (helper(nums1, nums2) + helper(nums1, nums2)) / 2.0;
        }
    }

    private int helper(int[] nums1, int[] nums2) {
        if (p1 < nums1.length && p2 < nums2.length) {
            if (nums1[p1] < nums2[p2]) {
                return nums1[p1++];
            } else {
                return nums2[p2++];
            }
        } else if (p1 < nums1.length) {
            return nums1[p1++];
        } else if (p2 < nums2.length) {
            return nums2[p2++];
        }
        return -1;
    }

}