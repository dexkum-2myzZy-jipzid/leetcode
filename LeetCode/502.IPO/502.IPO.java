class Solution {

    class Project {
        int profit;
        int capital;

        Project(int p, int c) {
            this.profit = p;
            this.capital = c;
        }
    }

    public int findMaximizedCapital(int k, int w, int[] profits, int[] capital) {
        PriorityQueue<Project> maxHeap = new PriorityQueue<>(
                (p1, p2) -> p2.profit - p1.profit);

        PriorityQueue<Project> minHeap = new PriorityQueue<>(
                (p1, p2) -> p1.capital - p2.capital);

        for (int i = 0; i < profits.length; i++) {
            Project p = new Project(profits[i], capital[i]);
            if (p.capital <= w) {
                maxHeap.add(p);
            } else {
                minHeap.add(p);
            }
        }

        int num = 0;
        while (num < k) {
            if (maxHeap.isEmpty()) {
                break;
            }

            w += maxHeap.remove().profit;
            num += 1;

            while (!minHeap.isEmpty() && minHeap.peek().capital <= w) {
                maxHeap.add(minHeap.remove());
            }
        }

        return w;
    }
}