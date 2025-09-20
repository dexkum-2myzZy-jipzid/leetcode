class Solution {
    public int countTriplets(int[] arr) {
        int n = arr.length;
        int[] xorArr = new int[n + 1];

        // Precompute the XOR prefix array
        for (int i = 1; i <= n; i++) {
            xorArr[i] = xorArr[i - 1] ^ arr[i - 1];
        }

        // System.out.println(Arrays.toString(xorArr));

        int result = 0;
        for (int i = 0; i < n; i++) {
            for (int k = i + 1; k < n; k++) {
                if (xorArr[i] == xorArr[k + 1]) {
                    result += (k - i);
                }
            }
        }

        return result;
    }
}
