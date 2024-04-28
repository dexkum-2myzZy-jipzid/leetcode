class Solution {
    public int minimumAddedInteger(int[] nums1, int[] nums2) {
        // sort
        Arrays.sort(nums1);
        Arrays.sort(nums2);

        // 3 scenarios min value
        int result = Integer.MAX_VALUE;
        for (int i = 0; i < 3; i++) {
            int min = nums1[i];
            int x = nums2[0] - min;

            // two points to compare nums2 is subsequence of nums1
            int k = 1;
            for (int j = i + 1; k < nums2.length && j < nums1.length; j++) {
                if (nums1[j] + x == nums2[k]) {
                    k += 1;
                }
            }

            if (k == nums2.length) {
                result = Math.min(result, x);
            }
        }

        return result;
    }
}