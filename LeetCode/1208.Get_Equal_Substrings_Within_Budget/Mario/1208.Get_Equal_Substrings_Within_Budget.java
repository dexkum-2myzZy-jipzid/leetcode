class Solution {
    public int equalSubstring(String s, String t, int maxCost) {
        int n = s.length();
        int[] cost = new int[n];
        for (int i = 0; i < n; i++) {
            cost[i] = Math.abs(t.charAt(i) - s.charAt(i));
        }

        // look for the max length subarray, sum <= maxCost
        // sliding window && two point
        int max = 0;
        int left = 0;
        int sum = 0;
        for (int i = 0; i < n; i++) {
            sum += cost[i];

            if (sum <= maxCost) {
                max = Math.max(max, (i - left) + 1);
            }

            while (sum > maxCost && left <= i) {
                sum -= cost[left];
                left += 1;
            }
        }

        return max;
    }
}