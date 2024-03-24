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