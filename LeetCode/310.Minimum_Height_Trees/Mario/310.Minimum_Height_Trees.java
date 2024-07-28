class Solution {
    public List<Integer> findMinHeightTrees(int n, int[][] edges) {
        // edge case
        if (n == 1) {
            List<Integer> result = new ArrayList<>();
            result.add(0);
            return result;
        }
        // create graph with adj list
        List<List<Integer>> graph = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            graph.add(new ArrayList<>());
        }
        int[] indegree = new int[n];
        for (int[] edge : edges) {
            int v1 = edge[0], v2 = edge[1];
            graph.get(v1).add(v2);
            graph.get(v2).add(v1);
            indegree[v1]++;
            indegree[v2]++;
        }

        Queue<Integer> queue = new LinkedList<>();
        for (int i = 0; i < n; i++) {
            if (indegree[i] == 1) {
                queue.offer(i);
            }
        }

        int leftLeaves = n;
        while (leftLeaves > 2) {
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                int v = queue.poll();
                leftLeaves -= 1;
                for (int nei : graph.get(v)) {
                    indegree[nei] -= 1;
                    if (indegree[nei] == 1) {
                        queue.offer(nei);
                    }
                }
            }
        }

        List<Integer> result = new ArrayList<>();
        while (!queue.isEmpty()) {
            result.add(queue.poll());
        }
        return result;
    }
}