class Solution {
    public int maxSubArray(int[] nums) {
        int current_max = 0, global_max = Integer.MIN_VALUE;

        for (int i = 0; i < nums.length; i++) {
            current_max += nums[i];
            if (current_max > global_max) {
                global_max = current_max;
            }

            if (current_max < 0) {
                current_max = 0;
            }
        }

        return global_max;
    }
}