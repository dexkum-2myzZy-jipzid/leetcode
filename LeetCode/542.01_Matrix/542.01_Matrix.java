class Solution {

    public int[][] updateMatrix(int[][] mat) {
        Queue<int[]> queue = new LinkedList<>();

        int m = mat.length, n = mat[0].length;
        boolean[][] v = new boolean[m][n];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (mat[i][j] != 0) {
                    mat[i][j] = -1;
                } else {
                    queue.offer(new int[] { i, j });
                    v[i][j] = true;
                }
            }
        }

        int[][] dirs = { { 1, 0 }, { 0, 1 }, { -1, 0 }, { 0, -1 } };
        while (!queue.isEmpty()) {
            int[] e = queue.poll();
            for (int[] dir : dirs) {
                int i = e[0] + dir[0], j = e[1] + dir[1];
                if (i >= 0 && i < m && j >= 0 && j < n && !v[i][j]) {
                    mat[i][j] = mat[e[0]][e[1]] + 1;
                    v[i][j] = true;
                    queue.offer(new int[] { i, j });
                }
            }
        }

        return mat;
    }
}