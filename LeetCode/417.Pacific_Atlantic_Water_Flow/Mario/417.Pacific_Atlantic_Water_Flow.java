class Solution {
    public List<List<Integer>> pacificAtlantic(int[][] heights) {
        int m = heights.length, n = heights[0].length;
        // check if reach pacific
        boolean[][] pac = new boolean[m][n];
        // check if reach atlantic
        boolean[][] alt = new boolean[m][n];

        // iterate - first/last row
        for (int i = 0; i < n; i++) {
            bfs(0, i, heights, pac);
            bfs(m - 1, i, heights, alt);
        }
        // iterate - first/last column
        for (int i = 0; i < m; i++) {
            bfs(i, 0, heights, pac);
            bfs(i, n - 1, heights, alt);
        }

        List<List<Integer>> result = new ArrayList<>();
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (pac[i][j] && alt[i][j]) {
                    result.add(Arrays.asList(i, j));
                }
            }
        }

        return result;
    }

    final int[][] dirs = new int[][] { { -1, 0 }, { 1, 0 }, { 0, -1 }, { 0, 1 } };

    private void bfs(int i, int j, int[][] hs, boolean[][] reach) {
        int m = hs.length, n = hs[0].length;
        Queue<int[]> queue = new LinkedList<>();
        reach[i][j] = true;
        queue.offer(new int[] { i, j });

        while (!queue.isEmpty()) {
            int[] p = queue.poll();

            for (int[] dir : dirs) {
                int x = p[0] + dir[0], y = p[1] + dir[1];
                if (x >= 0 && x < m && y >= 0 && y < n && hs[x][y] >= hs[p[0]][p[1]] && !reach[x][y]) {
                    reach[x][y] = true;
                    queue.offer(new int[] { x, y });
                }
            }
        }
    }
}