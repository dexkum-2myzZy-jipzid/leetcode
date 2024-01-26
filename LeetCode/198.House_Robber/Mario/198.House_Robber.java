class Solution {
    public int rob(int[] nums) {
        int n = nums.length;
        if (n == 0)
            return 0;
        if (n == 1)
            return nums[0];

        int[] res = new int[n];
        res[0] = nums[0];
        for (int i = 1; i < n; i++) {
            int j = i - 2;
            int k = i - 3;
            if (k >= 0) {
                res[i] = Math.max(res[j], res[k]) + nums[i];
            } else if (j == 0) {
                res[i] = res[j] + nums[i];
            } else if (j < 0) {
                res[i] = nums[i];
            }
        }
        return Math.max(res[n - 1], res[n - 2]);
    }
}