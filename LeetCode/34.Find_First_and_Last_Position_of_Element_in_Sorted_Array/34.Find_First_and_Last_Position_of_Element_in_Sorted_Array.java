class Solution {
    public int[] searchRange(int[] nums, int target) {
        int n = nums.length;
        int l = 0, r = n - 1;
        while (l <= r) {
            int m = (l + r) / 2;
            if (nums[m] == target) {
                r = m - 1;
            } else if (nums[m] > target) {
                r = m - 1;
            } else {
                l = m + 1;
            }
        }

        if (l < 0 || l > n - 1)
            return new int[] { -1, -1 };

        if (nums[l] != target)
            return new int[] { -1, -1 };

        int left = l;
        r = n - 1;
        while (l <= r) {
            int m = (l + r) / 2;
            if (nums[m] == target) {
                l = m + 1;
            } else if (nums[m] > target) {
                r = m - 1;
            } else {
                l = m + 1;
            }
        }

        return new int[] { left, r };
    }
}