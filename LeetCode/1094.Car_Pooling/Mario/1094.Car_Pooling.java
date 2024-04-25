class Solution {
    public boolean carPooling(int[][] trips, int capacity) {
        int n = 0, minFrom = 1001;
        for (int[] trip : trips) {
            n = Math.max(trip[2], n);
            minFrom = Math.min(trip[1], minFrom);
        }
        int[] diff = new int[n + 1];
        for (int[] trip : trips) {
            int num = trip[0], from = trip[1], to = trip[2];
            diff[from] += num;
            if (to < diff.length) {
                diff[to] -= num;
            }
        }

        int[] result = new int[n];
        result[minFrom] = diff[minFrom];
        int maxCapacity = result[minFrom];
        for (int i = minFrom + 1; i < n; i++) {
            result[i] = diff[i] + result[i - 1];
            maxCapacity = Math.max(maxCapacity, result[i]);
        }

        return maxCapacity <= capacity;
    }
}