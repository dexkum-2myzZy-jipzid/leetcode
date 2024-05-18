class Solution {
    public long[] minCost(int n, int[][] roads, int[] appleCost, int k) {
        // build graph
        List<List<int[]>> graph = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            graph.add(new ArrayList<int[]>());
        }

        for (int[] road : roads) {
            int startCity = road[0], endCity = road[1], cost = road[2];
            graph.get(startCity - 1).add(new int[] { endCity, cost });
            graph.get(endCity - 1).add(new int[] { startCity, cost });
        }

        // Like Dijsktra algorithm
        // 1. setup init value
        long[] result = new long[n];
        for (int i = 0; i < n; i++) {
            result[i] = appleCost[i];
        }

        PriorityQueue<long[]> heap = new PriorityQueue<>((a, b) -> Long.compare(a[0], b[0]));
        for (int i = 0; i < n; i++) {
            heap.offer(new long[] { appleCost[i], i });
        }

        // 2. Dijstra algo
        while (!heap.isEmpty()) {
            long[] element = heap.poll();
            long cost = element[0], startCity = element[1];
            int starInt = (int) startCity;

            if (result[starInt] < cost)
                continue;

            for (int[] nei : graph.get(starInt)) {
                if (result[nei[0] - 1] > nei[1] * (1 + k) + result[starInt]) {
                    result[nei[0] - 1] = nei[1] * (1 + k) + result[starInt];
                    heap.offer(new long[] { result[starInt], nei[0] - 1 });
                }
            }
        }

        return result;
    }
}