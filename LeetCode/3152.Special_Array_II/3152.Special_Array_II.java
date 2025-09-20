class Solution {
    public boolean[] isArraySpecial(int[] nums, int[][] queries) {
        int n = nums.length;
        boolean[] special = new boolean[n];

        for (int i = 0; i < n - 1; i++) {
            if (nums[i] % 2 == nums[i + 1] % 2) {
                special[i] = true;
            }
        }

        int[] prefix = new int[n];
        for (int i = 1; i < n; i++) {
            prefix[i] = prefix[i - 1] + (special[i - 1] ? 1 : 0);
        }

        boolean[] result = new boolean[queries.length];
        for (int i = 0; i < queries.length; i++) {
            int[] query = queries[i];
            int start = query[0], end = query[1];
            if (prefix[end] - prefix[start] == 0) {
                result[i] = true;
            }
        }

        return result;
    }
}