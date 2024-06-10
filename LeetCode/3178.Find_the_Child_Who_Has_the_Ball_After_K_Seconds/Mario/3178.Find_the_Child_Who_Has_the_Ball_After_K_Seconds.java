class Solution {
    public int numberOfChild(int n, int k) {
        int round = k / (n - 1);
        k %= (n - 1);
        if (round % 2 == 0) {
            return k;
        } else {
            return n - 1 - k;
        }
    }
}