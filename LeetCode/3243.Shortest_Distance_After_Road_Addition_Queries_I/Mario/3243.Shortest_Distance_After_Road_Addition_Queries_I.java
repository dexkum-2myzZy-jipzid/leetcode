class Solution {
    public int[] shortestDistanceAfterQueries(int n, int[][] queries) {
        // create graph with adj list
        List<List<Integer>> graph = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            graph.add(new ArrayList<>());
        }
        for (int i = 0; i < n - 1; i++) {
            graph.get(i).add(i + 1);
        }

        int m = queries.length;
        int[] result = new int[m];
        int[] visited = new int[n];
        Arrays.fill(visited, -1);
        for (int i = 0; i < m; i++) {
            int from = queries[i][0], to = queries[i][1];
            graph.get(from).add(to);
            // bfs path
            result[i] = bfs(i, n - 1, graph, visited);
        }

        return result;
    }

    private int bfs(int i, int end, List<List<Integer>> graph, int[] visited) {
        Queue<Integer> queue = new LinkedList<>();
        queue.offer(0);
        int path = 0;
        while (!queue.isEmpty()) {
            int size = queue.size();
            path += 1;
            for (int j = 0; j < size; j++) {
                int node = queue.poll();
                if (node == end) {
                    return path - 1;
                }
                for (int nei : graph.get(node)) {
                    if (visited[nei] != i) {
                        visited[nei] = i;
                        queue.offer(nei);
                    }
                }
            }
        }
        return -1;
    }
}