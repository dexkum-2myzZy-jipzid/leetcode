class Solution {
    public int[] advantageCount(int[] nums1, int[] nums2) {
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[0] - b[0]);
        int n = nums2.length;
        for (int i = 0; i < n; i++) {
            pq.offer(new int[] { nums2[i], i });
        }

        Arrays.sort(nums1);

        int[] result = new int[n];
        Arrays.fill(result, -1);

        Queue<Integer> queue = new LinkedList<>();
        for (int i = 0; i < n; i++) {
            int[] e = pq.peek();
            int val = e[0], j = e[1];
            if (nums1[i] <= val) {
                queue.offer(nums1[i]);
            } else {
                result[j] = nums1[i];
                pq.poll();
            }
        }

        for (int i = 0; i < n; i++) {
            if (result[i] == -1) {
                result[i] = queue.poll();
            }
        }

        return result;

    }
}