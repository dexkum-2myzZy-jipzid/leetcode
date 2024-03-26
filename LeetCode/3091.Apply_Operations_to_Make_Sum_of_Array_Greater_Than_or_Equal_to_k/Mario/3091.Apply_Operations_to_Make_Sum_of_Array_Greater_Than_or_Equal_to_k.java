class Solution {
    public int minOperations(int k) {
        int x = 0;
        int min = k - 1;
        while (x * x < k) {
            x += 1;
            int y = (k / x) + ((k % x) > 0 ? 1 : 0) - 1;
            min = Math.min(min, y + x - 1);
        }
        return min;
    }
}

// Another Solution
class Solution {
    // (k-1)/(x + 1) + x
    public int minOperations(int k) {
        double x = Math.max(Math.sqrt(k - 1), 1.0);
        int n = (int) Math.floor(x);
        return Math.min((k - 1) / n + n - 1, (k - 1) / (n + 1) + n);
    }
}