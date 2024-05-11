class Solution {
    public double mincostToHireWorkers(int[] quality, int[] wage, int k) {
        List<int[]> ratio = new ArrayList<>();

        for (int i = 0; i < quality.length; i++) {
            ratio.add(new int[] { quality[i], wage[i] });
        }

        ratio.sort((a, b) -> a[1] * b[0] - b[1] * a[0]);

        PriorityQueue<int[]> maxHeap = new PriorityQueue<>((a, b) -> b[0] - a[0]);

        double minCost = Double.MAX_VALUE;
        double totalQuality = 0;

        for (int[] r : ratio) {
            maxHeap.offer(r);
            totalQuality += r[0];
            double rate = (double) r[1] / (double) r[0];

            if (maxHeap.size() > k) {
                int[] maxQuality = maxHeap.poll();
                totalQuality -= maxQuality[0];
            }

            if (maxHeap.size() == k) {
                minCost = Math.min(minCost, rate * totalQuality);
            }
        }

        return minCost;
    }
}