class Solution {
    public int rob(int[] nums) {
        int n = nums.length;
        // edge case
        if (n == 1)
            return nums[0];
        if (n == 2)
            return Math.max(nums[0], nums[1]);

        // index: 0 -> n-2
        int[] dp1 = new int[n - 1];
        dp1[0] = nums[0];
        dp1[1] = Math.max(nums[0], nums[1]);
        for (int i = 2; i < n - 1; i++) {
            dp1[i] = Math.max(dp1[i - 2] + nums[i], dp1[i - 1]);
        }

        // index: 1 -> n-1
        int[] dp2 = new int[n - 1];
        dp2[0] = nums[1];
        dp2[1] = Math.max(nums[1], nums[2]);
        for (int i = 3; i < n; i++) {
            dp2[i - 1] = Math.max(dp2[i - 3] + nums[i], dp2[i - 2]);
        }

        // System.out.println(Arrays.toString(dp1));
        // System.out.println(Arrays.toString(dp2));

        return Math.max(dp1[n - 2], dp2[n - 2]);
    }
}