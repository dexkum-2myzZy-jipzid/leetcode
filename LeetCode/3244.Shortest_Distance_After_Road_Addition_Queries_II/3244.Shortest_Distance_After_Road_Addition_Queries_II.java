class Solution {
    // Intuition: Difference array, Union-Find, Interval merging, Dynamic
    // programming, Graphs (Dijkstra)
    // Find the shortest distance with the minimum number of sides, so you can union
    // the sides.
    public int[] shortestDistanceAfterQueries(int n, int[][] queries) {
        UnionFind uf = new UnionFind(n - 1);
        int m = queries.length;
        int[] result = new int[m];

        for (int i = 0; i < m; i++) {
            int from = queries[i][0], to = queries[i][1];
            for (int j = from; j < to; j++) {
                j = uf.find(j);
                uf.union(j, to - 1);
            }
            result[i] = uf.count;
        }

        return result;
    }
}

class UnionFind {
    int[] parent;
    int count;

    UnionFind(int n) {
        this.count = n;
        this.parent = new int[n];
        for (int i = 0; i < n; i++) {
            parent[i] = i;
        }
    }

    public int find(int x) {
        if (parent[x] != x) {
            parent[x] = find(parent[x]);
        }
        return parent[x];
    }

    public void union(int x, int y) {
        int rootX = find(x);
        int rootY = find(y);

        if (rootX != rootY) {
            count -= 1;
            parent[rootX] = rootY;
        }
    }
}