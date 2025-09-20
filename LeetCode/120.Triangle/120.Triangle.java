class Solution {
    public int minimumTotal(List<List<Integer>> triangle) {
        int n = triangle.size();
        int dp[][] = new int[n][n];
        for (int a[] : dp) {
            Arrays.fill(a, Integer.MAX_VALUE);
        }
        return findMinPathSum(triangle, 0, 0, n, dp);
    }

    public int findMinPathSum(List<List<Integer>> triangle, int i, int j, int n, int dp[][]) {
        // Base case: if we're at the last row, return the value at the current position
        if (i == n - 1) {
            return triangle.get(n - 1).get(j);
        }
        // If we've already calculated the minimum path sum for this position, return it
        if (dp[i][j] != Integer.MAX_VALUE) {
            return dp[i][j];
        }
        // Calculate the minimum path sum for the left and right child nodes
        int leftSum = findMinPathSum(triangle, i + 1, j, n, dp);
        int rightSum = findMinPathSum(triangle, i + 1, j + 1, n, dp);
        // The minimum path sum for the current position is the value at this position
        // plus the minimum of the left and right sums
        return dp[i][j] = triangle.get(i).get(j) + Math.min(leftSum, rightSum);
    }
}