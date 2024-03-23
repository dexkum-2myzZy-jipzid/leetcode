class Solution {
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        int[] left = new int[n];
        int[] right = new int[n];

        for (int i = 0; i < n; i++) {
            left[i] = i == 0 ? nums[i] : (nums[i] * left[i - 1]);
        }

        for (int i = n - 1; i >= 0; i--) {
            right[i] = (i == n - 1) ? nums[i] : (nums[i] * right[i + 1]);
        }

        int[] res = new int[n];
        for (int i = 0; i < n; i++) {
            int tmp = 1;
            if (i - 1 >= 0)
                tmp *= left[i - 1];
            if (i + 1 < n)
                tmp *= right[i + 1];
            res[i] = tmp;
        }

        return res;
    }
}