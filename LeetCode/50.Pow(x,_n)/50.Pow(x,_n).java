class Solution {
    public double myPow(double x, int n) {
        long m = n;
        return m >= 0 ? helper(x, m) : 1.0 / helper(x, -m);
    }

    private double helper(double x, long n) {
        if (n == 0) {
            return 1.0;
        }
        double y = helper(x, n / 2);
        return n % 2 == 0 ? y * y : y * y * x;
    }
}