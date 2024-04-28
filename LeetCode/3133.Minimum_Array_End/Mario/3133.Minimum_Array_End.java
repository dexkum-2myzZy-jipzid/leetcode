class Solution {
    public long minEnd(int n, int x) {
        n -= 1;
        long m = n, y = x;
        long j = 0;
        for (int i = 0; i < 64; i++) {
            long bit = (y >> i) & 1;
            if (bit == 0) {
                long nbit = (m >> j) & 1;
                y |= (nbit << i);
                j += 1;
            }
        }

        return y;
    }
}