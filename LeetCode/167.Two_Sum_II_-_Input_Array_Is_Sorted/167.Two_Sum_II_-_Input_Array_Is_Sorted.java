class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int n = numbers.length;
        int i = 0, j = n - 1, mid = 0;
        while (i < j) {
            mid = (i + j) / 2;
            int sum = numbers[i] + numbers[j];
            if (sum == target) {
                return new int[] { i + 1, j + 1 };
            } else if (sum > target) {
                if (numbers[i] + numbers[mid] > target) {
                    j = mid - 1;
                } else {
                    j -= 1;
                }
            } else {
                if (numbers[j] + numbers[mid] < target) {
                    i = mid + 1;
                } else {
                    i += 1;
                }
            }
        }

        return new int[] {};
    }
}
