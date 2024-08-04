class neighborSum {
    private int[][] grid;
    private int m;
    private int n;
    private Map<Integer, int[]> map;

    public neighborSum(int[][] grid) {
        this.grid = grid;
        this.m = grid.length;
        this.n = grid[0].length;
        this.map = new HashMap<>();
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                map.put(grid[i][j], new int[] { i, j });
            }
        }
    }

    public int adjacentSum(int value) {
        int[] loc = map.get(value);
        int x = loc[0], y = loc[1];
        int result = 0;
        // top
        if (x - 1 >= 0 && x - 1 < m) {
            result += grid[x - 1][y];
        }
        // bottom
        if (x + 1 >= 0 && x + 1 < m) {
            result += grid[x + 1][y];
        }
        // left
        if (y - 1 >= 0 && y - 1 < n) {
            result += grid[x][y - 1];
        }
        // right
        if (y + 1 >= 0 && y + 1 < n) {
            result += grid[x][y + 1];
        }
        return result;
    }

    public int diagonalSum(int value) {
        int[] loc = map.get(value);
        int x = loc[0], y = loc[1];
        int result = 0;
        // left top
        if (x - 1 >= 0 && x - 1 < m && y - 1 >= 0 && y - 1 < n) {
            result += grid[x - 1][y - 1];
        }
        // right top
        if (x - 1 >= 0 && x - 1 < m && y + 1 >= 0 && y + 1 < n) {
            result += grid[x - 1][y + 1];
        }
        if (x + 1 >= 0 && x + 1 < m && y - 1 >= 0 && y - 1 < n) {
            result += grid[x + 1][y - 1];
        }
        if (x + 1 >= 0 && x + 1 < m && y + 1 >= 0 && y + 1 < n) {
            result += grid[x + 1][y + 1];
        }
        return result;
    }
}

/**
 * Your neighborSum object will be instantiated and called as such:
 * neighborSum obj = new neighborSum(grid);
 * int param_1 = obj.adjacentSum(value);
 * int param_2 = obj.diagonalSum(value);
 */