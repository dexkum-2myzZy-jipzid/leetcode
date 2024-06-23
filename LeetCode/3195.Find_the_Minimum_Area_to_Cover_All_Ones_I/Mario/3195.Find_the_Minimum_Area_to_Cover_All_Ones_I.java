class Solution {
    public int minimumArea(int[][] grid) {
        int minX = Integer.MAX_VALUE, minY = Integer.MAX_VALUE;
        int maxX = Integer.MIN_VALUE, maxY = Integer.MIN_VALUE;

        int m = grid.length, n = grid[0].length;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 1) {
                    minX = Math.min(j, minX);
                    maxX = Math.max(j, maxX);
                    minY = Math.min(i, minY);
                    maxY = Math.max(i, maxY);
                }
            }
        }

        return (maxX - minX + 1) * (maxY - minY + 1);
    }
}