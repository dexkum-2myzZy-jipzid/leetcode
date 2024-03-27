class Solution {
    public int findMin(int[] nums) {
        int n = nums.length;
        int l = 0, r = n - 1;

        // remove left nums which == nums[n-1]
        while (l < r && nums[l] == nums[r]) {
            l += 1;
        }

        // binary search
        while (l < r) {
            int m = (l + r) / 2;
            if (nums[m] > nums[n - 1]) {
                l = m + 1;
            } else {
                r = m;
            }
        }

        return nums[l];
    }
}