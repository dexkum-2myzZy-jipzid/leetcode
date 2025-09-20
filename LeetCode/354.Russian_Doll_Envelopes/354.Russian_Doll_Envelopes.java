class Solution {
    public int maxEnvelopes(int[][] envelopes) {
        Arrays.sort(envelopes, (a, b) -> {
            return a[0] == b[0] ? b[1] - a[1] : a[0] - b[0];
        });

        int n = envelopes.length;
        int[] tops = new int[n];
        int piles = 0;
        for (int[] e : envelopes) {
            int num = e[1];

            int left = 0, right = piles;
            while (left < right) {
                int mid = (left + right) / 2;
                if (tops[mid] < num) {
                    left = mid + 1;
                } else {
                    right = mid;
                }
            }

            if (left == piles)
                piles += 1;
            tops[left] = num;
        }

        return piles;
    }
}