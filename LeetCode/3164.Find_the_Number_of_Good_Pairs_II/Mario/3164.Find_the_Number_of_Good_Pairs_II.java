class Solution {
    public long numberOfPairs(int[] nums1, int[] nums2, int k) {
        // map to store factor
        Map<Integer, Integer> counter = new HashMap<>();
        for (int num : nums1) {
            if (num % k != 0) {
                continue;
            }
            int val = num / k;
            for (int i = 1; i * i <= val; i++) {
                if (val % i == 0) {
                    int count = counter.getOrDefault(i, 0) + 1;
                    counter.put(i, count);
                    if (i * i < val) {
                        count = counter.getOrDefault(val / i, 0) + 1;
                        counter.put(val / i, count);
                    }
                }
            }
        }

        long result = 0;
        for (int num : nums2) {
            result += counter.getOrDefault(num, 0);
        }

        return result;
    }
}