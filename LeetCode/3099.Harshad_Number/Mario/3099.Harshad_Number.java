class Solution {
    public int sumOfTheDigitsOfHarshadNumber(int x) {
        int sum = 0;
        int value = x;
        while (value > 9) {
            sum += value % 10;
            value /= 10;
        }
        sum += value;

        if (sum == 0)
            return sum;

        if (x % sum == 0) {
            return sum;
        } else {
            return -1;
        }
    }
}