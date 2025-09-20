public class Solution {
    // you need to treat n as an unsigned value
    public int hammingWeight(int n) {
        int res = 0;
        for (int i = 0; i < 32; i++) {
            int bit = (n >> i) & 1;
            if (bit == 1) {
                res += 1;
            }
        }
        return res;
    }
}