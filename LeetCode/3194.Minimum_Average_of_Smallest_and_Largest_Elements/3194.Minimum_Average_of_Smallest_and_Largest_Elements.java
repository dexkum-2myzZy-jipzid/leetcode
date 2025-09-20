class Solution {
    public double minimumAverage(int[] nums) {
        Arrays.sort(nums);
        int n = nums.length;
        double minSum = 100;
        for (int i = 0; i < n / 2; i++) {
            double val = (double) (nums[i] + nums[n - 1 - i]);
            minSum = Math.min(minSum, val);
        }
        return minSum / 2;
    }
}