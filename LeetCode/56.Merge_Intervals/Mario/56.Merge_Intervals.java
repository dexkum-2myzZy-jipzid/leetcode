class Solution {
    public int[][] merge(int[][] intervals) {
        PriorityQueue<int[]> heap = new PriorityQueue<>((a, b) -> a[0] - b[0]);

        for (int[] interval : intervals) {
            heap.offer(interval);
        }

        Deque<int[]> q = new ArrayDeque<>();

        while (!heap.isEmpty()) {
            int[] first = heap.poll();
            if (q.isEmpty() || first[0] > q.peekLast()[1]) {
                q.offerLast(first);
            } else {
                int[] last = q.pollLast();
                last[0] = last[0];
                last[1] = Math.max(last[1], first[1]);
                heap.offer(last);
            }
        }

        int[][] res = new int[q.size()][2];
        for (int i = 0; i < res.length; i++) {
            res[i] = q.pollFirst();
        }

        return res;
    }
}