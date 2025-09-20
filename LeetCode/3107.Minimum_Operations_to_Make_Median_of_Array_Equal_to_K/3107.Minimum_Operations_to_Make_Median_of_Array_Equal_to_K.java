class Solution {
    public long minOperationsToMakeMedianK(int[] nums, int k) {
        Arrays.sort(nums);
        int n = nums.length;
        int m = n / 2;

        long ops = 0;
        if (k > nums[m]) {
            for (int i = m; i < n; i++) {
                if (nums[i] >= k) {
                    break;
                }
                ops += k - nums[i];
            }
        } else if (k < nums[m]) {
            for (int i = m; i >= 0; i--) {
                if (nums[i] <= k) {
                    break;
                }
                ops += nums[i] - k;
            }
        } else {
            return 0;
        }

        return ops;
    }
}