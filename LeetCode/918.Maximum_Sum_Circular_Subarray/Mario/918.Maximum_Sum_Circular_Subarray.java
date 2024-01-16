class Solution {
    public int maxSubarraySumCircular(int[] nums) {
        int total = 0, curMax = 0, sumMax = nums[0], curMin = 0, sumMin = nums[0];
        for (int n : nums) {
            curMax = Math.max(curMax + n, n);
            sumMax = Math.max(sumMax, curMax);
            curMin = Math.min(curMin + n, n);
            sumMin = Math.min(sumMin, curMin);
            total += n;
        }
        return sumMax > 0 ? Math.max(sumMax, total - sumMin) : sumMax;
    }
}