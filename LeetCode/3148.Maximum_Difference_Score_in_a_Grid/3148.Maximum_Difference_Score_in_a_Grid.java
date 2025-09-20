class Solution {
    public int maxScore(List<List<Integer>> grid) {
        int m = grid.size(), n = grid.get(0).size();

        int[][] maxGrid = new int[m][n];

        // init maxGrid
        maxGrid[m - 1][n - 1] = grid.get(m - 1).get(n - 1);

        // iterate
        for (int i = m - 1; i >= 0; i--) {
            for (int j = n - 1; j >= 0; j--) {
                maxGrid[i][j] = grid.get(i).get(j);
                if (i + 1 < m) {
                    maxGrid[i][j] = Math.max(maxGrid[i][j], maxGrid[i + 1][j]);
                }
                if (j + 1 < n) {
                    maxGrid[i][j] = Math.max(maxGrid[i][j], maxGrid[i][j + 1]);
                }
            }
        }

        int result = Integer.MIN_VALUE;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (i == m - 1 && j == n - 1) {
                    continue;
                }
                int diff = Integer.MIN_VALUE;
                int val = grid.get(i).get(j);
                if (i + 1 < m) {
                    diff = Math.max(maxGrid[i + 1][j] - val, diff);
                }
                if (j + 1 < n) {
                    diff = Math.max(maxGrid[i][j + 1] - val, diff);
                }

                result = Math.max(result, diff);
            }
        }

        return result;
    }
}