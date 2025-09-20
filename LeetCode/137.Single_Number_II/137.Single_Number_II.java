class Solution {
    public int singleNumber(int[] nums) {
        int res = 0;
        for (int i = 0; i < 32; i++) {
            int cnt = 0;
            for (int num : nums) {
                cnt += (num >> i) & 1;
            }
            res |= (cnt % 3) << i;
        }
        return res;
    }
}