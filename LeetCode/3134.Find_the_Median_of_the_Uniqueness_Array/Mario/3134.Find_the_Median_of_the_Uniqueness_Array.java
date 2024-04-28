class Solution {
    public int medianOfUniquenessArray(int[] nums) {
        int n = nums.length;
        int left = 1, right = n;
        long total = (long) (n + 1) * n / 2;
        while (left < right) {
            int mid = (left + right) / 2;
            if (atmost(nums, mid) * 2 >= total) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }

        return left;
    }

    private long atmost(int[] nums, int k) {
        long res = 0;
        Map<Integer, Integer> count = new HashMap<>();
        int i = 0;
        for (int j = 0; j < nums.length; j++) {
            count.put(nums[j], count.getOrDefault(nums[j], 0) + 1);
            while (count.size() > k) {
                count.put(nums[i], count.get(nums[i]) - 1);
                if (count.get(nums[i]) == 0) {
                    count.remove(nums[i]);
                }
                i++;
            }
            res += j - i + 1;
        }
        return res;
    }
}