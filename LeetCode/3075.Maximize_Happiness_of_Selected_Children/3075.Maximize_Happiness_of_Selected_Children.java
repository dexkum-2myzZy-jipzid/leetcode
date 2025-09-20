class Solution {
    public long maximumHappinessSum(int[] happiness, int k) {
        // sort to decrease
        Arrays.sort(happiness);

        int n = happiness.length;
        long result = 0;
        int minusNum = 0;
        for (int i = n - 1; i > n - k - 1; i--) {
            if (happiness[i] - minusNum > 0) {
                result += happiness[i] - minusNum;
                minusNum += 1;
            } else {
                break;
            }
        }

        return result;
    }
}