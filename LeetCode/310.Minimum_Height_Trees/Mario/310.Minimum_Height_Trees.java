class Solution {
    public List<Integer> findMinHeightTrees(int n, int[][] edges) {
        // handle corner case
        if (n < 2) {
            List<Integer> result = new ArrayList<>();
            for (int i = 0; i < n; i++) {
                result.add(i);
            }
            return result;
        }
        // build graph
        List<List<Integer>> graph = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            graph.add(new ArrayList<>());
        }
        for (int[] edge : edges) {
            graph.get(edge[0]).add(edge[1]);
            graph.get(edge[1]).add(edge[0]);
        }

        List<Integer> leaves = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            List<Integer> list = graph.get(i);
            if (list.size() == 1)
                leaves.add(i);
        }

        int remaningLeaves = n;
        while (remaningLeaves > 2) {
            remaningLeaves -= leaves.size();
            List<Integer> newLeaves = new ArrayList<>();
            for (Integer leaf : leaves) {
                // leaves only has one indegree
                int neighbor = graph.get(leaf).get(0);
                graph.get(neighbor).remove(leaf);
                if (graph.get(neighbor).size() == 1)
                    newLeaves.add(neighbor);
            }

            leaves = newLeaves;
        }

        return leaves;
    }
}