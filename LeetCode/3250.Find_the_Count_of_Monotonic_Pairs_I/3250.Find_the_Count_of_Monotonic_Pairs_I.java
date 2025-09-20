class Solution {
    private int[][] matrix;
    private int MOD = 1000000007;

    public int countOfPairs(int[] nums) {
        // init matrix
        int n = nums.length;
        matrix = new int[n][51];
        for (int[] arr : matrix) {
            Arrays.fill(arr, -1);
        }

        long sum = 0;
        for (int i = nums[0]; i >= 0; i--) {
            sum += dfs(1, nums, i);
            sum %= MOD;
        }

        return (int) sum;
    }

    private int dfs(int i, int[] nums, int k) {
        if (i == nums.length) {
            return 1;
        }

        if (matrix[i][k] >= 0) {
            return matrix[i][k];
        }

        // k = arr2[i-1]
        // 0 < cur <= arr2[i-1] = k
        // cur + arr1[i] = nums[i]
        // arr1[i] >= nums[i-1] - arr2[i-1]

        // cur <= k
        // cur <= nums[i] - nums[i-1] + k
        int max = Math.min(k, nums[i] - nums[i - 1] + k);
        long sum = 0;
        for (int j = max; j >= 0; j--) {
            sum += dfs(i + 1, nums, j);
            sum %= MOD;
        }

        matrix[i][k] = (int) sum % MOD;

        return matrix[i][k];
    }
}