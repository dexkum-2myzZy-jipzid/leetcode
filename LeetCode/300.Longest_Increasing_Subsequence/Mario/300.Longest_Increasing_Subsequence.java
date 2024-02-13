class Solution {
    public int lengthOfLIS(int[] nums) {
        int[] dp = new int[nums.length];
        int max = 1;

        for (int i = 0; i < nums.length; i++) {
            int localMax = 1;
            for (int j = 0; j < i; j++) {
                if (nums[i] > nums[j]) {
                    localMax = Math.max(localMax, dp[j] + 1);
                }
            }
            dp[i] = localMax;
            if (localMax > max)
                max = localMax;
        }
        return max;
    }
}

// binary search
class Solution {
    public int lengthOfLIS(int[] nums) {
        int n = nums.length;
        int[] top = new int[n];

        int piles = 0;
        for (int num : nums) {
            int left = 0, right = piles;

            while (left < right) {
                int mid = (left + right) / 2;
                if (top[mid] < num) {
                    left = mid + 1;
                } else {
                    right = mid;
                }
            }

            if (left == piles) {
                piles += 1;
            }
            top[left] = num;
        }

        return piles;
    }
}