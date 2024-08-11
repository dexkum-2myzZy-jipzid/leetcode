class Solution {
    int count = 0;
    int[] vals;

    public int countGoodNodes(int[][] edges) {
        // create graph
        int n = edges.length + 1;
        vals = new int[n];
        Arrays.fill(vals, -1);

        List<List<Integer>> graph = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            graph.add(new ArrayList<>());
        }
        for (int[] e : edges) {
            graph.get(e[0]).add(e[1]);
            graph.get(e[1]).add(e[0]);
        }

        // dfs
        dfs(0, -1, graph);

        return count;
    }

    private int dfs(int val, int parent, List<List<Integer>> graph) {
        if (vals[val] != -1) {
            return vals[val];
        }

        List<Integer> neis = graph.get(val);

        int sum = 0;
        boolean same = true;
        for (int i = 0; i < neis.size(); i++) {
            int nei = neis.get(i);
            if (nei == parent) {
                continue;
            }
            if (vals[nei] == -1) {
                vals[nei] = dfs(nei, val, graph) + 1;
            }
            sum += vals[nei];
            if (vals[nei] != vals[neis.get(0)]) {
                System.out.println("nei:" + vals[nei] + "\t 0:" + vals[neis.get(0)]);
                same = false;
            }
        }

        if (same) {
            count += 1;
        }

        return sum;
    }

}