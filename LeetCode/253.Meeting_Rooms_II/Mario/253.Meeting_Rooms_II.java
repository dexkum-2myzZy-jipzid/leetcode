class Solution {
    public int minMeetingRooms(int[][] intervals) {
        int n = intervals.length;
        Arrays.sort(intervals, (a, b) -> (a[0] - b[0]));

        PriorityQueue<Integer> pq = new PriorityQueue<>();
        pq.offer(intervals[0][1]);

        for (int i = 1; i < n; i++) {
            int[] current = intervals[i];

            if (current[0] >= pq.peek()) {
                pq.poll();
            }

            pq.offer(current[1]);
        }

        return pq.size();
    }
}