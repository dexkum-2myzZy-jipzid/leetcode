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

// segment tree
class Solution {
    public long[] mostFrequentIDs(int[] nums, int[] freq) {
        // value in nums map to index
        Map<Integer, Integer> idxMap = new HashMap<>();

        int index = 0;
        for (int n : nums) {
            Integer i = idxMap.get(n);
            if (i == null) {
                idxMap.put(n, index);
                index += 1;
            }
        }

        // System.out.println(idxMap);

        // create segment tree
        int n = idxMap.size();
        long[] tree = new long[n * 2];

        // iterate nums & freq
        long[] res = new long[nums.length];
        for (int i = 0; i < nums.length; i++) {
            int num = nums[i], fre = freq[i];
            int idx = idxMap.get(num);
            int j = idx + n;
            tree[j] += fre;
            // update segment tree
            while (j / 2 >= 1) {
                int k = j / 2;
                if ((2 * k + 1) >= 2 * n) {
                    tree[k] = tree[j];
                } else {
                    tree[k] = Math.max(tree[2 * k], tree[2 * k + 1]);
                }
                j = k;
            }

            // System.out.println(Arrays.toString(tree));
            res[i] = tree[1];
        }

        return res;
    }
}
