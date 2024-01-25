class Solution {
    public int trailingZeroes(int n) {
        int t = n / 5;
        int res = t;
        while (t >= 5) {
            t /= 5;
            res += t;
        }
        return res;
    }
}