class Solution {
    public int[] kthSmallestPrimeFraction(int[] arr, int k) {
        // binary search, left = 0, right = 1.0
        double left = 0, right = 1.0;
        int n = arr.length;

        // compare left and right,
        while (left < right) {

            double mid = (left + right) / 2.0;
            int count = 0, j = 1;
            double fraction = 0.0;
            int numeratorIdx = 0, denominatorIdx = 0;
            // double for loop count then num of fractions smaller than mid
            for (int i = 0; i < n; i++) {
                while (j < n && arr[i] >= mid * arr[j]) {
                    j++;
                }

                count += n - j;

                if (j == n)
                    break;

                double tmp = (double) arr[i] / arr[j];
                if (tmp > fraction) {
                    fraction = tmp;
                    numeratorIdx = i;
                    denominatorIdx = j;
                }
            }

            // if num is bigger than k, right = mid
            // num is smaller than k, left = mid
            // num == k, return new int[]{nums[i], nums[j]}
            if (count == k) {
                return new int[] { arr[numeratorIdx], arr[denominatorIdx] };
            } else if (count > k) {
                right = mid;
            } else {
                left = mid;
            }

        }

        return new int[] {};
    }
}