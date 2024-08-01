class Solution {
    public int networkBecomesIdle(int[][] edges, int[] patience) {
        // all node get shortest path from master server 0
        // dist:[0, 1, 2] patience:[0, 2, 1]
        // eg, server 2, (2*2)/1 = 4, send 4 messages, so 4s + (2 * 2) = 8s

        // create graph using adj list
        int n = patience.length;
        List<List<Integer>> graph = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            graph.add(new ArrayList<>());
        }
        for (int[] e : edges) {
            graph.get(e[0]).add(e[1]);
            graph.get(e[1]).add(e[0]);
        }

        // bfs first to get shortest path
        int[] dist = new int[n];
        Arrays.fill(dist, -1);
        dist[0] = 0;
        Queue<Integer> queue = new LinkedList<>();
        queue.offer(0);
        while (!queue.isEmpty()) {
            int node = queue.poll();
            for (int nei : graph.get(node)) {
                if (dist[nei] == -1) {
                    dist[nei] = dist[node] + 1;
                    queue.offer(nei);
                }
            }
        }

        // System.out.println(Arrays.toString(dist));
        int result = 0;
        for (int i = 1; i < n; i++) {
            int path = dist[i] * 2, pat = patience[i];
            int numOfPatience = path / pat;
            if (path % pat == 0) {
                numOfPatience -= 1;
            }
            result = Math.max(result, numOfPatience * pat + path);
        }

        return result + 1;
    }
}