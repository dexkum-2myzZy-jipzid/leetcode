class Solution {
    public long sumDigitDifferences(int[] nums) {
        // get count of digits
        int n = 0, tmp = nums[0];
        while (tmp > 0) {
            tmp /= 10;
            n += 1;
        }
        // System.out.println(n);

        long result = 0;
        for (int i = 0; i < n; i++) {
            int[] digits = new int[nums.length];
            for (int j = 0; j < nums.length; j++) {
                digits[j] = nums[j] % 10;
                nums[j] /= 10;
            }

            result += countDigit(digits);
        }

        return result;
    }

    private long countDigit(int[] digits) {

        int[] count = new int[10];
        int total = 0;
        for (int i = 0; i < digits.length; i++) {
            count[digits[i]] += 1;
            total += 1;
        }
        // System.out.println(Arrays.toString(count));
        long result = 0;
        for (int i = 0; i < 10; i++) {
            result += count[i] * (total - count[i]);

        }
        return result / 2;
    }
}