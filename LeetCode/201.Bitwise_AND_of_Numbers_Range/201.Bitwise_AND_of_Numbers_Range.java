class Solution {
    public int rangeBitwiseAnd(int left, int right) {
        int move = 0;
        while (left < right) {
            left >>= 1;
            right >>= 1;
            move += 1;
        }
        return left << move;
    }
}