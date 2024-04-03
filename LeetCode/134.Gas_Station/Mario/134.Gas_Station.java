class Solution {
    public int canCompleteCircuit(int[] gas, int[] cost) {
        int currGain = 0, totalGain = 0, res = 0;

        for (int i = 0; i < gas.length; i++) {
            int gain = gas[i] - cost[i];
            totalGain += gain;
            currGain += gain;

            if (currGain < 0) {
                res = i + 1;
                currGain = 0;
            }
        }

        return totalGain >= 0 ? res : -1;
    }
}