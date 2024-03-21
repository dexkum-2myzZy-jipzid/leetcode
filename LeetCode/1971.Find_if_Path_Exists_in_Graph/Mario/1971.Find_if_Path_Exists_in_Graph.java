class Solution {
    public boolean validPath(int n, int[][] edges, int source, int destination) {
        int[] parent = new int[n];
        for (int i = 0; i < n; i++) {
            parent[i] = i;
        }

        for (int[] edge : edges) {
            union(parent, edge[0], edge[1]);
        }

        return find(parent, source) == find(parent, destination);
    }

    private int find(int[] parent, int x) {
        if (parent[x] != x) {
            return find(parent, parent[x]);
        }
        return x;
    }

    private void union(int[] parent, int x, int y) {
        int a = find(parent, x), b = find(parent, y);
        if (a != b) {
            parent[a] = b;
        }
    }
}