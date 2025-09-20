class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        int i = 0, j = 0;
        int n = nums.length;
        int minLen = n + 1;
        int sum = nums[0];
        while (j < n) {
            if (sum >= target) {
                if (j - i + 1 < minLen)
                    minLen = j - i + 1;
                sum -= nums[i];
                i += 1;
            } else {
                j += 1;
                if (j < n)
                    sum += nums[j];
            }
        }
        return minLen == n + 1 ? 0 : minLen;
    }
}