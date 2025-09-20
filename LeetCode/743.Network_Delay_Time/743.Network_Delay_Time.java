class Solution {
    public int networkDelayTime(int[][] times, int n, int k) {
        record Vertex(int num, int time) {
        }
        ;
        // create graph
        List<List<Vertex>> graph = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            graph.add(new ArrayList<>());
        }

        for (int[] t : times) {
            graph.get(t[0] - 1).add(new Vertex(t[1] - 1, t[2]));
        }

        PriorityQueue<Vertex> maxHeap = new PriorityQueue<>((a, b) -> (b.time - a.time));
        maxHeap.add(new Vertex(k - 1, 0));
        int[] results = new int[n];
        Arrays.fill(results, Integer.MAX_VALUE);
        results[k - 1] = 0;
        while (!maxHeap.isEmpty()) {
            Vertex v = maxHeap.poll();
            for (Vertex nei : graph.get(v.num)) {
                int num = nei.num, time = nei.time;
                if (results[num] > time + v.time) {
                    results[num] = time + v.time;
                    maxHeap.offer(new Vertex(num, results[num]));
                }
            }
        }

        int ans = 0;
        for (int i = 0; i < n; i++) {
            if (results[i] == Integer.MAX_VALUE) {
                return -1;
            } else {
                ans = Math.max(results[i], ans);
            }
        }

        return ans;
    }
}