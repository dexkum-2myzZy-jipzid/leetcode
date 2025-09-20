class NumMatrix {

    // f(i, j) = f(i-1, j) + f(i, j-1) - f(i-1, j-1) + m(i, j)
    private int[][] prefixSum;

    public NumMatrix(int[][] matrix) {
        int m = matrix.length, n = matrix[0].length;
        prefixSum = new int[m][n];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                prefixSum[i][j] = matrix[i][j];
                if (i - 1 >= 0) {
                    prefixSum[i][j] += prefixSum[i - 1][j];
                }
                if (j - 1 >= 0) {
                    prefixSum[i][j] += prefixSum[i][j - 1];
                }
                if (i - 1 >= 0 && j - 1 >= 0) {
                    prefixSum[i][j] -= prefixSum[i - 1][j - 1];
                }
            }
        }
    }

    public int sumRegion(int row1, int col1, int row2, int col2) {
        int res = prefixSum[row2][col2];
        if (row2 >= 0 && col1 - 1 >= 0) {
            res -= prefixSum[row2][col1 - 1];
        }
        if (row1 - 1 >= 0 && col2 >= 0) {
            res -= prefixSum[row1 - 1][col2];
        }
        if (row1 - 1 >= 0 && col1 - 1 >= 0) {
            res += prefixSum[row1 - 1][col1 - 1];
        }
        return res;
    }
}

/**
 * Your NumMatrix object will be instantiated and called as such:
 * NumMatrix obj = new NumMatrix(matrix);
 * int param_1 = obj.sumRegion(row1,col1,row2,col2);
 */