class Solution {
    public int[] plusOne(int[] digits) {
        int plus = 0;
        for (int i = digits.length - 1; i > -1; i--) {
            int val = digits[i] + plus + (i == digits.length - 1 ? 1 : 0);
            if (val > 9) {
                plus = 1;
                val %= 10;
            } else {
                plus = 0;
            }
            digits[i] = val;
        }
        if (plus == 1) {
            int[] res = new int[digits.length + 1];
            res[0] = plus;
            for (int i = 1; i < res.length; i++) {
                res[i] = digits[i - 1];
            }
            return res;
        }
        return digits;
    }
}