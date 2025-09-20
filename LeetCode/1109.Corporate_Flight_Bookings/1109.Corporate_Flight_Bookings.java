class Solution {
    public int[] corpFlightBookings(int[][] bookings, int n) {
        int[] diff = new int[n];
        for (int[] booking : bookings) {
            int left = booking[0], right = booking[1], num = booking[2];
            diff[left - 1] += num;
            if (right < diff.length) {
                diff[right] -= num;
            }
        }

        int[] result = new int[n];
        result[0] = diff[0];
        for (int i = 1; i < n; i++) {
            result[i] = result[i - 1] + diff[i];
        }

        return result;
    }
}