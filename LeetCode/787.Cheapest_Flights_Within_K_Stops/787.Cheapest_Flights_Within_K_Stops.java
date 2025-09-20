class Solution {
    public int findCheapestPrice(
            int n,
            int[][] flights,
            int src,
            int dst,
            int k) {
        // create graph using adj list
        List<List<int[]>> graph = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            graph.add(new ArrayList<>());
        }
        for (int[] f : flights) {
            graph.get(f[0]).add(new int[] { f[1], f[2] });
        }

        // dijstra algo
        PriorityQueue<Flight> pq = new PriorityQueue<>((a, b) -> {
            if (a.k == b.k) {
                return a.weight - b.weight;
            } else {
                return a.k - b.k;
            }
        });
        pq.offer(new Flight(src, 0, 0));

        // store every stop weights
        int[] weights = new int[n];
        Arrays.fill(weights, Integer.MAX_VALUE);
        weights[src] = 0;

        while (!pq.isEmpty()) {
            Flight f = pq.poll();
            if (f.k > k)
                continue;
            for (int[] nei : graph.get(f.num)) {
                int num = nei[0], weight = nei[1] + f.weight;
                if (weight < weights[num]) {
                    weights[num] = weight;
                    pq.offer(new Flight(num, weight, f.k + 1));
                }
            }
        }

        return weights[dst] == Integer.MAX_VALUE ? -1 : weights[dst];
    }
}

class Flight {
    int num;
    int weight;
    int k;

    Flight(int num, int weight, int k) {
        this.num = num;
        this.weight = weight;
        this.k = k;
    }
}