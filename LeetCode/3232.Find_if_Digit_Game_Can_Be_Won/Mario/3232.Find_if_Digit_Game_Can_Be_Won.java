class Solution {
    public boolean canAliceWin(int[] nums) {

        int singleDigitSum = 0, sum = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] < 10) {
                singleDigitSum += nums[i];
            }
            sum += nums[i];
        }

        int doubleDigitSum = sum - singleDigitSum;
        if (doubleDigitSum == singleDigitSum) {
            return false;
        } else {
            return true;
        }
    }
}