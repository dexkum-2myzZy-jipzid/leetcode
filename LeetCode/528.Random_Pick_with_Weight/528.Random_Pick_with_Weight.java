class Solution {
    private int[] prefixSum;
    private int totalSum;

    public Solution(int[] w) {
        int n = w.length;
        this.prefixSum = new int[n];
        prefixSum[0] = w[0];
        for (int i = 1; i < n; i++) {
            prefixSum[i] = w[i] + prefixSum[i - 1];
        }
        this.totalSum = prefixSum[n - 1];
    }

    public int pickIndex() {
        double val = totalSum * Math.random();
        // find index in prefixSum array
        int left = 0, right = prefixSum.length;
        while (left < right) {
            int mid = (left + right) / 2;
            if (prefixSum[mid] < val) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }

        return left;
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(w);
 * int param_1 = obj.pickIndex();
 */