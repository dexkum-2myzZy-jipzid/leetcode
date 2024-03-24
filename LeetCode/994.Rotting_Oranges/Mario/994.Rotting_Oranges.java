class Solution {
    public int orangesRotting(int[][] grid) {
        // oranges count
        int fresh = 0;
        Queue<int[]> q = new LinkedList<>();
        int m = grid.length, n = grid[0].length;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                int val = grid[i][j];
                if (val == 1) {
                    fresh += 1;
                }
                if (val == 2) {
                    int[] point = new int[] { i, j };
                    q.offer(point);
                }
            }
        }

        if (fresh == 0) {
            return 0;
        }

        // bfs
        int[][] dirs = { { 1, 0 }, { 0, 1 }, { -1, 0 }, { 0, -1 } };
        int minutes = 0;
        while (!q.isEmpty()) {
            int len = q.size();
            for (int i = 0; i < len; i++) {
                int[] last = q.poll();
                for (int[] d : dirs) {
                    int x = last[0] + d[0], y = last[1] + d[1];
                    int[] next = new int[] { x, y };
                    if (x >= 0 && x < m && y >= 0 && y < n && grid[x][y] == 1) {
                        grid[x][y] = 2;
                        q.offer(next);
                        fresh -= 1;
                    }
                }

            }
            if (q.size() > 0) {
                minutes += 1;
            }
        }

        return fresh > 0 ? -1 : minutes;
    }

}