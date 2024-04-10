class Solution {
    public int[] minimumCost(int n, int[][] edges, int[][] query) {
        // create union find & store weights
        UnionFind uf = new UnionFind(n);
        for (int[] e : edges) {
            uf.union(e[0], e[1], e[2]);
        }

        // query vertices
        int[] res = new int[query.length];
        for (int i = 0; i < query.length; i++) {
            res[i] = uf.query(query[i][0], query[i][1]);
        }

        return res;
    }
}

class UnionFind {
    private int[] parent;
    private int[] size;
    private int[] weights;

    UnionFind(int n) {
        parent = new int[n];
        size = new int[n];
        weights = new int[n];
        for (int i = 0; i < n; i++) {
            parent[i] = i;
            size[i] = 1;
            weights[i] = -1;
        }
    }

    int find(int i) {
        if (parent[i] == i) {
            return i;
        }
        return find(parent[i]);
    }

    void union(int a, int b, int weight) {
        int pa = find(a);
        int pb = find(b);
        if (pa == pb) {
            weights[pa] = weights[pb] = weights[pa] & weights[pb] & weight;
            return;
        }

        if (size[pa] < size[pb]) {
            size[pa] += size[pb];
            parent[pa] = pb;
        } else {
            size[pb] += size[pa];
            parent[pb] = pa;
        }
        weights[pa] = weights[pb] = weights[pa] & weights[pb] & weight;
    }

    int query(int a, int b) {
        int pa = find(a);
        int pb = find(b);
        if (pa != pb) {
            return -1;
        } else {
            return weights[pa];
        }
    }
}