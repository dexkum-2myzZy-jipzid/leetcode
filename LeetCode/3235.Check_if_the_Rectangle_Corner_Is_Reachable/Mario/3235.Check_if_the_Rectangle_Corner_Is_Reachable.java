class Solution {
    public boolean canReachCorner(int X, int Y, int[][] circles) {
        int m = circles.length;
        // top edge && left edge(m),
        // bottom edge && right edge(m+1),
        UnionFind uf = new UnionFind(m + 2);
        for (int i = 0; i < m; i++) {
            int[] circle = circles[i];
            int x = circle[0], y = circle[1], r = circle[2];
            // check connectivity to the top or left edge
            if (y + r >= Y || x <= r) {
                uf.union(i, m);
            }
            // check connectivity to the bottom or right edge
            if (y <= r || x + r >= X) {
                uf.union(i, m + 1);
            }

            // check ith circle connectivity to others circles
            for (int j = 0; j < i; j++) {
                int[] other = circles[j];
                int dx = x - other[0];
                int dy = y - other[1];
                int distanceSquared = dx * dx + dy * dy;
                int radiusSum = r + other[2];

                if (distanceSquared <= radiusSum * radiusSum) {
                    uf.union(i, j);
                }
            }

            if (uf.find(m) == uf.find(m + 1)) {
                return false;
            }
        }

        return true;
    }
}

class UnionFind {
    int[] parent;

    UnionFind(int n) {
        this.parent = new int[n];
        for (int i = 0; i < n; i++) {
            parent[i] = i;
        }
    }

    public int find(int x) {
        if (x != parent[x]) {
            parent[x] = find(parent[x]);
        }
        return parent[x];
    }

    public void union(int x, int y) {
        parent[find(x)] = find(y);
    }
}