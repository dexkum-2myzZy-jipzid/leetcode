class Solution {
    public long[] mostFrequentIDs(int[] nums, int[] freq) {
        PriorityQueue<long[]> pq = new PriorityQueue<>((a, b) -> (int) (b[1] - a[1]));
        HashMap<Long, Long> map = new HashMap<>();

        long[] res = new long[nums.length];
        for (int i = 0; i < nums.length; i++) {
            long n = nums[i];
            long f = map.getOrDefault(n, 0L) + freq[i];
            map.put(n, f);

            long[] value = new long[] { n, map.get(n) };
            pq.offer(value);
            while (pq.peek()[1] != map.get(pq.peek()[0])) {
                pq.poll();
            }

            res[i] = pq.peek()[1];
        }

        return res;
    }
}
