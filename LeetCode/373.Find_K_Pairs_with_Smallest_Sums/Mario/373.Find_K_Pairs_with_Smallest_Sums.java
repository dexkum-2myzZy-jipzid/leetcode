class Solution {
    public List<List<Integer>> kSmallestPairs(int[] nums1, int[] nums2, int k) {
        int n = nums1.length, m = nums2.length;
        List<List<Integer>> res = new ArrayList<>();
        PriorityQueue<int[]> pq = new PriorityQueue<>(k,
                (a, b) -> (a[0] - b[0]));
        pq.add(new int[] { nums1[0] + nums2[0], 0, 0 });
        while (!pq.isEmpty() && res.size() < k) {
            int[] e = pq.poll();
            int i = e[1], j = e[2];
            res.add(List.of(nums1[i], nums2[j]));
            if (j == 0 && i + 1 < n)
                pq.add(new int[] { nums1[i + 1] + nums2[j], i + 1, j });
            if (j + 1 < m)
                pq.add(new int[] { nums1[i] + nums2[j + 1], i, j + 1 });
        }
        return res;
    }
}