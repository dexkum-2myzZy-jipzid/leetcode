class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        // left = 1, right = max(piles)
        int left = 1, right = -1;
        for (int p : piles) {
            right = Math.max(right, p);
        }

        // binary search
        while (left < right) {
            int mid = (left + right) / 2;
            long hours = getHours(piles, mid);
            // System.out.println("hours:" + hours + " mid:" + mid + " left:" + left + "
            // right:" + right);
            if (hours <= h) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }

        // left = right
        // while (getHours(piles, left) > h) {
        // left += 1;
        // }

        return left;
    }

    private long getHours(int[] piles, int k) {
        long hours = 0;
        for (int p : piles) {
            hours += (p / k);
            if (p % k > 0)
                hours += 1;
        }
        return hours;
    }
}